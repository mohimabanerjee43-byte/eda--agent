import pandas as pd


def scaledown(df: pd.DataFrame) -> pd.DataFrame:
    """
    Simulates ScaleDown by compressing metadata and optimizing dataframe
    """

    print("📉 Applying ScaleDown on dataset metadata...")

    # Downcast numeric columns
    for col in df.select_dtypes(include=["int64", "float64"]).columns:
        df[col] = pd.to_numeric(df[col], downcast="float")

    # Convert object columns to category
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype("category")

    print("✅ ScaleDown completed (metadata compressed)")

    return df