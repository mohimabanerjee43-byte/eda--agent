def recommend_model(df, target_column):
    if df[target_column].dtype == "object":
        return {
            "problem": "classification",
            "models": ["Logistic Regression", "Random Forest", "XGBoost"]
        }
    else:
        return {
            "problem": "regression",
            "models": ["Linear Regression", "Random Forest", "LightGBM"]
        }