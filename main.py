import os
import sys
import pandas as pd


try:
    from loaders.csv_loader import load_csv
except:
    print("⚠ csv_loader not found")
    load_csv = None

try:
    from agents.visualization_agent import run_visualizations
except:
    run_visualizations = None

try:
    from agents.insight_agent import detect_anomalies, recommend_features
except:
    detect_anomalies = None
    recommend_features = None

try:
    from agents.automl_agent import recommend_model
except:
    recommend_model = None

try:
    from reports.report_generator import generate_report
except:
    generate_report = None



# Config

DATA_PATH = "data/data.csv"     
TARGET_COLUMN = "Attrition"     



# Main Pipeline

def main():
    print("🚀 Starting EDA Agent Pipeline...")

    # 1. Load Data
    if load_csv is None:
        print("❌ CSV loader missing")
        return

    if not os.path.exists(DATA_PATH):
        print(f"❌ Data file not found: {DATA_PATH}")
        return

    df = load_csv(DATA_PATH)
    print(f"✅ Data loaded | Shape: {df.shape}")

    # 2. Visualization
    if run_visualizations:
        try:
            print("📊 Running Visualization Agent...")
            run_visualizations(df)
            print("✅ Visualization Agent Completed")
        except Exception as e:
            print("⚠ Visualization skipped:", e)

    # 3. Insights
    anomalies = None
    features = None

    if detect_anomalies:
        try:
            anomalies = detect_anomalies(df)
            print("🔍 Anomaly detection completed")
        except Exception as e:
            print("⚠ Anomaly detection skipped:", e)

    if recommend_features:
        try:
            features = recommend_features(df)
            print("🧠 Feature recommendation completed")
        except Exception as e:
            print("⚠ Feature recommendation skipped:", e)

    # 4. AutoML (optional target)
    model_info = None

    if recommend_model:
        if TARGET_COLUMN in df.columns:
            try:
                model_info = recommend_model(df, TARGET_COLUMN)
                print("🤖 Model recommendation completed")
            except Exception as e:
                print("⚠ AutoML skipped:", e)
        else:
            print(f"⚠ Target column '{TARGET_COLUMN}' not found — skipping AutoML")

    # 5. Report
    if generate_report:
        try:
            generate_report(
                df=df,
                anomalies=anomalies,
                features=features,
                model_info=model_info
            )
            print("📄 Report generated successfully")
        except Exception as e:
            print("⚠ Report generation skipped:", e)

    print("🎉 EDA Agent Pipeline Completed Successfully!")



if __name__ == "__main__":
    main()