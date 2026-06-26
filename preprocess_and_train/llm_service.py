from langchain_groq import ChatGroq
from tavily import TavilyClient
from pydantic import BaseModel
import pandas as pd  
import os  
from dotenv import load_dotenv
from logger import get_logger

logger = get_logger(__name__)

from pydantic import BaseModel
from typing import List


class OutputSchema(BaseModel):
    dataset_type: str

    best_model: str

    important_features: List[str]

    key_insights: List[str]

    future_trends: List[str]

    business_insights: List[str]

    risks: List[str]

    next_actions: List[str]
    
def insights_service(df, target_column, topic):
    
    load_dotenv()
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
    
    if not GROQ_API_KEY and TAVILY_API_KEY:
        logger.error("API Keys Missing")
        raise RuntimeError("API keys Missing")
    data_frame = df
    
    duplicates = data_frame.duplicated().sum()
    target_corr = (
    data_frame.select_dtypes(include="number")
      .corr()[target_column]
      .sort_values(ascending=False)
      .to_dict()
)
    
    dataset_summary = {
    "rows": len(df),
    "columns": len(df.columns),
    "target": target_column,
    "missing_values": df.isnull().sum().to_dict(),
    "top_correlations": dict(
        list(target_corr.items())[:10]
    ),
    "duplicates": duplicates,
}
    
    tavily_agent = TavilyClient(api_key=TAVILY_API_KEY)
    recent_trends = tavily_agent.search(query=f"Trends and Recent News About This Topic - {topic}", max_results=3)
    
    trend_context = "\n\n".join(
    f"Title: {r.get('title', '')}\n"
    f"Content: {r.get('content', '')[:300]}"
    for r in recent_trends.get("results", [])
)
    PROMPT = f"""
Analyze the following dataset summary and recent domain trends.
Dataset:
{dataset_summary}
Recent Trends:
{trend_context}
Target:
{target_column}
Provide:
1. Dataset overview
2. Key patterns and correlations
3. Data quality issues (missing values, outliers, imbalance, leakage)
4. Recommended preprocessing steps
5. Feature engineering suggestions
6. Best machine learning model only recommend one
7. Impact of recent trends on predictions
8. Future trends and risks
9. Actionable business insights
Be specific, data-driven, and concise.
    """
    
    client = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.3-70b-versatile")
    
    structured_llm = client.with_structured_output(OutputSchema)
    response = structured_llm.invoke(PROMPT)
    
    return response
