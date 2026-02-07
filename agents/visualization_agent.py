import os
import matplotlib.pyplot as plt
import seaborn as sns


def run_visualizations(df, output_dir="reports"):
    print("📊 Visualization Agent Started")

    os.makedirs(output_dir, exist_ok=True)

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    categorical_cols = df.select_dtypes(include=["object"]).columns

    # Numeric histograms
    for col in numeric_cols:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f"{col} Distribution")
        file_path = os.path.join(output_dir, f"{col}_hist.png")
        plt.savefig(file_path)
        plt.close()
        print(f"Saved: {file_path}")

    # Categorical bar charts
    for col in categorical_cols:
        if df[col].nunique() <= 10:
            plt.figure()
            df[col].value_counts().plot(kind="bar")
            plt.title(f"{col} Distribution")
            file_path = os.path.join(output_dir, f"{col}_bar.png")
            plt.savefig(file_path)
            plt.close()
            print(f"Saved: {file_path}")

    print("✅ Visualization Agent Completed")