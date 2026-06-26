param_grids = {
    # Logistic Regression
    "Logistic Regression": {
        "C": [0.01, 0.1, 1, 10, 100],
        "penalty": ["l1", "l2", "elasticnet", None],
        "solver": ["liblinear", "saga"],
        "max_iter": [100, 500, 1000]
    },

    # Linear Regression
    "Linear Regression": {
        "fit_intercept": [True, False],
        "positive": [True, False]
    },

    # Decision Tree Classifier
    "Decision Tree": {
        "criterion": ["gini", "entropy", "log_loss"],
        "max_depth": [None, 5, 10, 15, 20, 25],
        "min_samples_split": [2, 5, 10, 20],
        "min_samples_leaf": [1, 2, 4, 8],
        "max_features": [None, "sqrt", "log2"],
        "splitter": ["best", "random"]
    },

    # Decision Tree Regressor
    "Decision Tree Regressor": {
        "criterion": ["squared_error", "friedman_mse", "absolute_error", "poisson"],
        "max_depth": [None, 5, 10, 15, 20, 25],
        "min_samples_split": [2, 5, 10, 20],
        "min_samples_leaf": [1, 2, 4, 8],
        "max_features": [None, "sqrt", "log2"]
    },

    # KNN Classifier
    "KNN": {
        "n_neighbors": [3, 5, 7, 9, 11, 15],
        "weights": ["uniform", "distance"],
        "algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
        "p": [1, 2]
    },

    # KNN Regressor
    "KNN Regressor": {
        "n_neighbors": [3, 5, 7, 9, 11, 15],
        "weights": ["uniform", "distance"],
        "algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
        "p": [1, 2]
    },

    # SVC
    "SVM": {
        "C": [0.1, 1, 10, 100],
        "kernel": ["linear", "poly", "rbf", "sigmoid"],
        "degree": [2, 3, 4],
        "gamma": ["scale", "auto"],
        "coef0": [0.0, 0.1, 0.5]
    },

    # SVR
    "SVR": {
        "C": [0.1, 1, 10, 100],
        "kernel": ["linear", "poly", "rbf", "sigmoid"],
        "degree": [2, 3, 4],
        "gamma": ["scale", "auto"],
        "epsilon": [0.01, 0.1, 0.5, 1.0],
        "coef0": [0.0, 0.1, 0.5]
    },

    # Random Forest Classifier
    "Random Forest": {
        "n_estimators": [50, 100, 200, 300],
        "criterion": ["gini", "entropy", "log_loss"],
        "max_depth": [None, 5, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", "log2", None],  # "auto" deprecated
        "bootstrap": [True, False]
    },

    # Random Forest Regressor
    "Random Forest Regressor": {
        "n_estimators": [50, 100, 200, 300],
        "criterion": ["squared_error", "absolute_error", "friedman_mse", "poisson"],
        "max_depth": [None, 5, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", "log2", None],  # "auto" deprecated
        "bootstrap": [True, False]
    }
}