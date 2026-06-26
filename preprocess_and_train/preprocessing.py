import sys
from pathlib import Path

project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
from sklearn.model_selection import train_test_split,RandomizedSearchCV
from models import classification_models, regression_models
from grids import param_grids
from sklearn.metrics import classification_report,mean_absolute_error,mean_squared_error,r2_score
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from logger import get_logger
import joblib

logger = get_logger(__name__)

def preprocess_and_eval(df, t_col, data_type, model_name): 
    """_summary_

    Args:
        df (_type_): _description_
        t_col (_type_): _description_
        data_type (_type_): _description_
    """
        
    data_frame = df
    
    X_col = data_frame.drop(columns=[t_col])
    y_col = data_frame[t_col]
    
    X_train, X_test, y_train, y_test = train_test_split(X_col, y_col, test_size=0.23, random_state=42)
    logger.info("Data Splitted")
    numeric_features = X_train.select_dtypes(include=["number"]).columns.tolist()
    categorical_features = X_train.select_dtypes(include=["category","object"]).columns.tolist()
    
    numeric_transforms = Pipeline(steps=[
        ("Imputaion", SimpleImputer(strategy="mean")),
        ("Scaling", StandardScaler())
    ])
    categorical_transforms = Pipeline(steps=[
        ("Imputation", SimpleImputer(strategy="most_frequent")),
        ("Encoding", OneHotEncoder(sparse_output=False, handle_unknown="ignore"))
    ])
    
    preprocess = ColumnTransformer(
        transformers=[
            ("Numeric",numeric_transforms, numeric_features),
            ("Category",categorical_transforms, categorical_features)
        ]
    )
    logger.info("Preprocessing Done")
    if data_type.lower() == "classification":
        selected_model = classification_models.get(model_name)
        logger.info("Classification Model Selected")
    else:
        selected_model = regression_models.get(model_name)
        logger.info("Regression Model Selected")
        
    pipeline = Pipeline(
        steps=[
            ("preprocess", preprocess),
            ("training", RandomizedSearchCV(selected_model, param_grids[model_name], n_iter=100))
        ]
    )
    
    trained_model = pipeline.fit(X_train, y_train)
    logger.info("Model trained")
    
    joblib.dump(trained_model, "model/trained_model.pkl")
    logger.info("Model Saved")
    
    pred = pipeline.predict(X_test)
    
    if data_type.lower() == "classification":
        Classification_report = classification_report(y_test, pred)
        logger.info("Classification Report Generated")
        return Classification_report
    else:
        r2 = r2_score(y_test, pred)
        mse = mean_squared_error(y_test, pred)
        mae  = mean_absolute_error(y_test, pred)
        Regression_report = f'''
            "Root Mean Squared Error": {mse**0.5},
            "R2 Score":{r2},
            "Mean Squared Error":{mse},
            "Mean Absolute Error":{mae}
        '''
        logger.info("Regression Report Generated")
        return Regression_report