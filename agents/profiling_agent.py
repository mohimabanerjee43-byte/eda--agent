import pandas as pd

def profile_dataframe(df: pd.DataFrame):
    profile = {}

    profile["rows"] = df.shape[0]
    profile["columns"] = df.shape[1]
    profile["dtypes"] = df.dtypes.astype(str).to_dict()
    profile["missing"] = df.isnull().sum().to_dict()
    profile["describe"] = df.describe(include="all").to_dict()

    return profile