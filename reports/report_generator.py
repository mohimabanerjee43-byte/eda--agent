import os
import json
from datetime import datetime

def generate_report(df, anomalies=None, features=None, model_info=None):
    # Ensure reports folder exists
    REPORT_DIR = "reports"
    os.makedirs(REPORT_DIR, exist_ok=True)

    report = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "dataset_shape": df.shape,
        "columns": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "anomalies": anomalies if anomalies is not None else "Not generated",
        "recommended_features": features if features is not None else "Not generated",
        "model_recommendation": model_info if model_info is not None else "Not generated"
    }

    report_path = os.path.join(REPORT_DIR, "eda_report.json")

    with open(report_path, "w") as f:
        json.dump(report, f, indent=4)

    print(f"✅ Report saved to: {report_path}")