import pandas as pd
import numpy as np


def detect_anomalies(df):
    """
    Simple anomaly detection using z-score
    """
    anomalies = {}

    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        mean = df[col].mean()
        std = df[col].std()

        if std == 0:
            continue

        z_scores = (df[col] - mean) / std
        anomalies[col] = df[np.abs(z_scores) > 3][col].tolist()

    return anomalies


def recommend_features(df):
    """
    Feature engineering suggestions
    """
    suggestions = []

    numeric_cols = df.select_dtypes(include=np.number).columns
    categorical_cols = df.select_dtypes(exclude=np.number).columns

    if len(numeric_cols) > 1:
        suggestions.append("Create interaction features between numeric columns")

    if len(categorical_cols) > 0:
        suggestions.append("Apply one-hot encoding to categorical features")

    suggestions.append("Check skewness and apply log/box-cox transforms if needed")

    return suggestions