import numpy as np
import pandas as pd

def detect_anomalies(df: pd.DataFrame):
    anomalies = {}

    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        z_scores = (df[col] - df[col].mean()) / df[col].std()
        outliers = df[np.abs(z_scores) > 3]
        anomalies[col] = len(outliers)

    return anomalies