# 🤖 Data Scientist Assistant

An intelligent, end-to-end ML automation tool that takes raw data and delivers trained models, evaluation reports, and LLM-powered insights — all in one pipeline.

---

## 🧠 What It Does

**Data Scientist Assistant** automates the entire data science workflow:

1. **Upload a dataset** via the Streamlit frontend
2. **Auto-preprocess** — handles missing values, encoding, and scaling
3. **Train & tune** — runs `RandomizedSearchCV` across 10+ sklearn models
4. **Evaluate** — returns classification reports or regression metrics
5. **Get AI insights** — LLM (LLaMA 3.3 via Groq) + live web trends (Tavily) analyze your dataset and return structured business intelligence

---

## 🗂️ Project Structure

```
DATA_SCIENTIST/
├── Backend/
│   └── server.py                   # FastAPI backend server
├── Frontend/
│   ├── pages/
│   │   └── preprocessing_&_insights.py   # Streamlit preprocessing + insights page
│   └── Home.py                     # Streamlit home page
├── preprocess_and_train/
│   ├── __init__.py
│   ├── grids.py                    # Hyperparameter grids for all models
│   ├── llm_service.py              # Groq LLM + Tavily web search insights
│   ├── models.py                   # sklearn model definitions
│   └── preprocessing.py            # Full preprocessing + training pipeline
├── model/
│   └── trained_model.pkl           # Saved trained model (joblib)
├── logs/
│   └── app.log                     # Application logs
├── logger.py                       # Centralized logger
├── .env                            # API keys (not committed)
├── .gitignore
├── .python-version
├── pyproject.toml
└── requirements.txt
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| ML Models | scikit-learn |
| Hyperparameter Tuning | RandomizedSearchCV |
| LLM | LLaMA 3.3 70B via Groq API |
| Web Search | Tavily API |
| Structured Output | LangChain + Pydantic |
| Model Persistence | joblib |
| Environment | python-dotenv |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/data-scientist-assistant.git
cd data-scientist-assistant
```

### 2. Set Up Environment

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API Keys

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

> Get your Groq key at [console.groq.com](https://console.groq.com) and Tavily key at [tavily.com](https://tavily.com)

### 4. Run the App

**Start the FastAPI backend:**
```bash
uvicorn Backend.server:app --reload
```

**Start the Streamlit frontend:**
```bash
streamlit run Frontend/Home.py
```

---

## 🤖 Supported Models

### Classification
| Model | Key Hyperparameters Tuned |
|---|---|
| Logistic Regression | C, penalty, solver, max_iter |
| Decision Tree | criterion, max_depth, min_samples_split |
| KNN | n_neighbors, weights, algorithm, p |
| SVM (SVC) | C, kernel, degree, gamma |
| Random Forest | n_estimators, max_depth, max_features |

### Regression
| Model | Key Hyperparameters Tuned |
|---|---|
| Linear Regression | fit_intercept, positive |
| Decision Tree Regressor | criterion, max_depth, min_samples_split |
| KNN Regressor | n_neighbors, weights, algorithm |
| SVR | C, kernel, epsilon, gamma |
| Random Forest Regressor | n_estimators, max_depth, max_features |

---

## 📊 LLM Insight Engine

The `insights_service` in `llm_service.py` does the following:

- Computes dataset stats: shape, missing values, duplicates, top feature correlations
- Fetches **live domain trends** via Tavily web search
- Sends everything to **LLaMA 3.3 70B** (via Groq) with structured output parsing

**Returns a structured `OutputSchema` with:**

```python
dataset_type        # Classification or Regression
best_model          # Recommended model
important_features  # Key predictive features
key_insights        # Patterns and correlations found
future_trends       # Domain trends from web search
business_insights   # Actionable recommendations
risks               # Data quality issues and risks
next_actions        # Step-by-step next steps
```

---

## 📈 Evaluation Metrics

**Classification:**
- Precision, Recall, F1-Score (via `classification_report`)

**Regression:**
- R² Score
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)

---

## 🔧 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Groq API key for LLaMA 3.3 inference |
| `TAVILY_API_KEY` | Tavily API key for live web search |

---

## 📋 Requirements

See `requirements.txt` for the full list. Key dependencies:

```
scikit-learn
fastapi
uvicorn
streamlit
langchain-groq
tavily-python
pydantic
pandas
joblib
python-dotenv
```

---

## 🙌 Author

**Anuu** — AI Engineer & BCA Student  
Building intelligent ML pipelines and RAG systems.

[![GitHub](https://img.shields.io/badge/GitHub-your--username-black?logo=github)](https://github.com/Anurag07-crypto)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/anurag-kumar-69aa7838a/)

---

## 📄 License

This project is licensed under the MIT License.