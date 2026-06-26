import streamlit as st
import pandas as pd
import requests
import io

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Data Insights & ML", page_icon="🤖")

# ─────────────────────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────────────────────

def get_insights(uploaded_file, target_column, topic):
    """Send file to backend and get insights."""
    try:
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
        data = {
            "target_column": target_column,
            "topic": topic
        }
        response = requests.post(
            f"{BACKEND_URL}/insights",
            files=files,
            data=data,
            timeout=120
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Backend connection failed: {str(e)}")
        return None

def preprocess_data(uploaded_file, target_column, model_name, data_type):
    """Send file to backend for preprocessing & model training."""
    try:
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
        data = {
            "t_col": target_column,
            "model_name": model_name,
            "data_type": data_type
        }
        response = requests.post(
            f"{BACKEND_URL}/uploads",
            files=files,
            data=data,
            timeout=600
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Backend connection failed: {str(e)}")
        return None

# ─────────────────────────────────────────────────────────────
# Session State
# ─────────────────────────────────────────────────────────────

if "insights_result" not in st.session_state:
    st.session_state.insights_result = None
if "best_model" not in st.session_state:
    st.session_state.best_model = None
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "pd_df" not in st.session_state:
    st.session_state.pd_df = None

# ─────────────────────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────────────────────

with st.sidebar:
    st.title("⚙️ Navigation")
    st.markdown("---")
    st.markdown("**Step 1:** Upload your CSV")
    st.markdown("**Step 2:** Get AI Insights")
    st.markdown("**Step 3:** Preprocess & Train Model")
    st.markdown("---")
    st.info("💡 The **Insights** step recommends the best model for your data. Use that recommendation in the **Preprocessing** step.")

# ─────────────────────────────────────────────────────────────
# Main Title
# ─────────────────────────────────────────────────────────────

st.title("🤖 AI-Powered Data Insights & ML Pipeline")
st.markdown("Upload a CSV, get AI insights with model recommendations, then preprocess and train your model.")
st.markdown("---")

# ─────────────────────────────────────────────────────────────
# STEP 0: File Upload (Shared for both sections)
# ─────────────────────────────────────────────────────────────

st.header("📤 Step 0: Upload Your Dataset")

uploaded_file = st.file_uploader("Upload CSV Here", type=["csv"], key="main_uploader")

if uploaded_file is not None:
    # Read CSV only once and store in session state
    if st.session_state.uploaded_file is None or st.session_state.uploaded_file.name != uploaded_file.name:
        st.session_state.uploaded_file = uploaded_file
        st.session_state.pd_df = pd.read_csv(uploaded_file)
        st.session_state.insights_result = None  # Reset insights on new file
        st.session_state.best_model = None
        st.rerun()

    pd_df = st.session_state.pd_df
    
    st.success(f"✅ File uploaded: **{uploaded_file.name}** | Shape: `{pd_df.shape}`")
    
    with st.expander("🔍 Preview Data"):
        st.dataframe(pd_df.head(10), use_container_width=True)
        st.markdown(f"**Columns:** {', '.join(pd_df.columns.tolist())}")
        st.markdown(f"**Data Types:**")
        st.write(pd_df.dtypes)
    
    st.markdown("---")
    
    # ═══════════════════════════════════════════════════════
    # STEP 1: INSIGHTS (FIRST)
    # ═══════════════════════════════════════════════════════
    
    st.header("📊 Step 1: Get AI Insights & Model Recommendation")
    st.markdown("Let our AI analyze your data and recommend the best machine learning model.")
    
    with st.form(key="insights_form"):
        st.subheader("🔧 Configure Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            target_column_insights = st.selectbox(
                "Select Target Column",
                options=pd_df.columns.tolist(),
                key="insights_target"
            )
        with col2:
            topic = st.text_input(
                "Analysis Topic",
                placeholder="e.g., Sales Forecasting, Customer Churn, Fraud Detection",
                key="insights_topic"
            )
        
        submitted_insights = st.form_submit_button("🚀 Generate Insights & Get Model Recommendation")
        
        if submitted_insights:
            if not topic:
                st.warning("⚠️ Please enter an analysis topic.")
            else:
                with st.spinner("⏳ AI is analyzing your data... This may take up to 2 minutes."):
                    uploaded_file.seek(0)
                    result = get_insights(uploaded_file, target_column_insights, topic)
                
                if result:
                    st.session_state.insights_result = result.get("response")
                    st.session_state.best_model = result.get("best_model")
                    st.success("✅ Insights generated successfully!")
                    st.rerun()
    
    # Display insights result if available
    if st.session_state.insights_result:
        st.markdown("---")
        st.subheader("📝 AI Insights Report")
        st.info(f"🏆 **Recommended Best Model:** `{st.session_state.best_model}`")
        st.markdown("Use this model name in the Preprocessing step below.")
        st.markdown("---")
        st.markdown(st.session_state.insights_result)
        st.markdown("---")
    
    # ═══════════════════════════════════════════════════════
    # STEP 2: PREPROCESSING & MODEL TRAINING (SECOND)
    # ═══════════════════════════════════════════════════════
    
    st.header("⚙️ Step 2: Preprocess Data & Train Model")
    st.markdown("Use the model recommendation from Step 1, or choose your own.")
    
    # Available models
    available_models = [
        "Auto (Let system choose)",
        "Logistic Regression",
        "Random Forest Classifier",
        "Random Forest Regressor",
        "XGBoost Classifier",
        "XGBoost Regressor",
        "Support Vector Machine",
        "K-Nearest Neighbors",
        "Decision Tree",
        "Gradient Boosting",
        "AdaBoost",
        "Naive Bayes",
        "Linear Regression",
        "Ridge Regression",
        "Lasso Regression"
    ]
    
    with st.form(key="preprocess_form"):
        st.subheader("🔧 Configure Preprocessing & Training")
        
        col1, col2 = st.columns(2)
        with col1:
            target_column_preprocess = st.selectbox(
                "Select Target Column",
                options=pd_df.columns.tolist(),
                key="preprocess_target"
            )
        with col2:
            data_type = st.selectbox(
                "Data Type / Problem Type",
                options=["Auto-detect", "Classification", "Regression", "Clustering", "Time Series"],
                help="Choose the type of ML problem. 'Auto-detect' lets the system decide."
            )
        
        # Model selection with recommendation highlight
        st.markdown("---")
        st.subheader("🎯 Model Selection")
        
        if st.session_state.best_model:
            st.success(f"💡 **AI Recommendation from Insights:** Use **`{st.session_state.best_model}`**")
            # Try to pre-select the recommended model
            recommended_index = 0
            for i, model in enumerate(available_models):
                if st.session_state.best_model.lower() in model.lower():
                    recommended_index = i
                    break
        else:
            st.info("ℹ️ Run Step 1 (Insights) first to get a model recommendation.")
            recommended_index = 0
        
        model_name = st.selectbox(
            "Choose Model",
            options=available_models,
            index=recommended_index,
            help="Select a model. The AI-recommended model is pre-selected if available."
        )
        
        # Advanced preprocessing options
        st.markdown("---")
        st.subheader("🔧 Preprocessing Options")
        
        col3, col4, col5 = st.columns(3)
        with col3:
            handle_missing = st.selectbox(
                "Handle Missing Values",
                options=["Auto", "Drop rows", "Mean imputation", "Median imputation", "Mode imputation", "Forward fill"]
            )
        with col4:
            encode_categorical = st.selectbox(
                "Encode Categorical",
                options=["Auto", "One-Hot Encoding", "Label Encoding", "Target Encoding"]
            )
        with col5:
            scale_features = st.selectbox(
                "Scale Features",
                options=["Auto", "StandardScaler", "MinMaxScaler", "RobustScaler", "None"]
            )
        
        col6, col7 = st.columns(2)
        with col6:
            test_size = st.slider("Test Split Ratio", min_value=0.1, max_value=0.5, value=0.2, step=0.05)
        with col7:
            random_state = st.number_input("Random State", min_value=0, max_value=9999, value=42)
        
        submitted_preprocess = st.form_submit_button("⚙️ Preprocess & Train Model")
        
        if submitted_preprocess:
            if model_name == "Auto (Let system choose)" and not st.session_state.best_model:
                st.warning("⚠️ Please either run Insights first or select a specific model.")
            else:
                # Use recommended model if "Auto" is selected
                final_model = st.session_state.best_model if model_name == "Auto (Let system choose)" and st.session_state.best_model else model_name
                
                with st.spinner(f"⏳ Training model: **{final_model}**... This may take a few minutes."):
                    uploaded_file.seek(0)
                    result = preprocess_data(uploaded_file, target_column_preprocess, final_model, data_type)
                
                if result:
                    st.success("✅ Model trained successfully!")
                    st.markdown("---")
                    st.subheader("📈 Training Report")
                    st.markdown(result.get("response", "No report available."))
                    st.download_button("Download trained Model",data="model/trained_model.pkl")
    
else:
    st.info("📤 Please upload a CSV file to begin.")
    
    # Show a sample workflow illustration
    st.markdown("---")
    st.subheader("📋 How It Works")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**1️⃣ Upload CSV**")
        st.markdown("Upload your dataset in CSV format.")
    with col2:
        st.markdown("**2️⃣ Get AI Insights**")
        st.markdown("AI analyzes your data and recommends the best model.")
    with col3:
        st.markdown("**3️⃣ Train Model**")
        st.markdown("Preprocess data and train using the recommended model.")
