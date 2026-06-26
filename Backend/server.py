from fastapi import FastAPI, HTTPException, File, UploadFile, Form
import uvicorn
import pandas as pd
from io import StringIO
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from preprocess_and_train.preprocessing import preprocess_and_eval
from preprocess_and_train.llm_service import insights_service
from logger import get_logger

logger = get_logger(__name__)
app = FastAPI(title="Data Insights API", version="1.0.0")

@app.post("/insights")
async def insights(
    target_column: str = Form(...),
    topic: str = Form(...),
    file: UploadFile = File(...)
):
    """
    Generate insights from uploaded CSV file.

    - **target_column**: The column to analyze/predict
    - **topic**: Topic/context for the analysis
    - **file**: CSV file to analyze
    """
    try:
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode("utf-8")))

        response = insights_service(df, target_column, topic)

        final_message = f"""
📊 Dataset Analysis Summary

Dataset Type: {response.dataset_type}

🏆 Best Model
{response.best_model}

🔑 Important Features
{chr(10).join(f"- {feature}" for feature in response.important_features)}

💡 Key Insights
{chr(10).join(f"- {insight}" for insight in response.key_insights)}

📈 Future Trends
{chr(10).join(f"- {trend}" for trend in response.future_trends)}

🏢 Business Insights
{chr(10).join(f"- {insight}" for insight in response.business_insights)}

⚠️ Risks
{chr(10).join(f"- {risk}" for risk in response.risks)}

🚀 Recommended Next Actions
{chr(10).join(f"- {action}" for action in response.next_actions)}
"""
        logger.info("Insights generated from backend side")
        return {
            "response": final_message,
            "best_model": response.best_model
        }

    except RuntimeError as e:
        logger.error(f"Runtime error in /insights: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    except UnicodeEncodeError as e:
        logger.error(f"Unicode encoding error in /insights: {e}")
        raise HTTPException(status_code=500, detail="Error processing response with special characters")
    except Exception as e:
        logger.error(f"Unexpected error in /insights: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Something went wrong. Please try again."
        )

@app.post("/uploads")
async def upload_files(
    t_col: str = Form(...),
    model_name: str = Form(...),
    data_type: str = Form(...),
    file: UploadFile = File(...)
):
    """
    Upload CSV and train a machine learning model.

    - **t_col**: Target column name
    - **model_name**: Name of the model to use
    - **data_type**: Type of the dataset
    - **file**: CSV file to process
    """
    try:
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode("utf-8")))

        report = preprocess_and_eval(df, t_col, data_type, model_name)
        logger.info("Machine Learning Model Generated from Backend Side")
        return {
            "response": report
        }
    except RuntimeError as e:
        logger.error(f"Runtime error in /uploads: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    except UnicodeEncodeError as e:
        logger.error(f"Unicode encoding error in /uploads: {e}")
        raise HTTPException(status_code=500, detail="Error processing response with special characters")
    except Exception as e:
        logger.error(f"Unexpected error in /uploads: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Something went wrong. Please try again."
        )

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, host="0.0.0.0", reload=False)