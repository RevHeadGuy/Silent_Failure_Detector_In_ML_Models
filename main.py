from monitoring.prediction_drift import compute_prediction_drift
from monitoring.drift_severity import classify_prediction_drift
from monitoring.feature_monitor import monitor_features
from config.config_loader import load_config
from src.load_data import load_dataset, split_baseline_monitoring
from model.train_model import train_model
from baseline.save_baseline_predictions import save_baseline_behavior
from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np

# Load config
config = load_config()
prediction_thresholds = config["thresholds"]["prediction_drift"]

# Load and split data
print("Loading data...")
df = load_dataset()
baseline_df, monitoring_df = split_baseline_monitoring(df)

# Train model
print("Training model...")
model, scaler = train_model(baseline_df)

# Save baseline behavior
print("Saving baseline predictions...")
save_baseline_behavior(model, scaler, baseline_df)

# Monitor prediction drift
print("Monitoring prediction drift...")
pred_drift = compute_prediction_drift(model, scaler, monitoring_df)

severity = classify_prediction_drift(pred_drift, prediction_thresholds)

print("Prediction Drift Metrics:", pred_drift)
print("⚠️ Drift Severity:", severity)

# Persist prediction drift metrics for the dashboard
baseline_dir = Path("baseline")
baseline_dir.mkdir(exist_ok=True)

drift_metrics_path = baseline_dir / "prediction_drift_metrics.csv"
timestamp = datetime.utcnow()

drift_row = pd.DataFrame(
    [
        {
            "timestamp": timestamp,
            "mean_shift": pred_drift.get("mean_shift", 0.0),
            "std_shift": pred_drift.get("std_shift", 0.0),
            "distribution_distance": pred_drift.get(
                "distribution_distance", 0.0
            ),
            "severity": severity,
        }
    ]
)

if drift_metrics_path.exists():
    drift_row.to_csv(drift_metrics_path, mode="a", header=False, index=False)
else:
    drift_row.to_csv(drift_metrics_path, index=False)

# Feature-level drift monitoring and persistence
print("Monitoring feature-level drift...")
feature_results, feature_alerts = monitor_features(baseline_df, monitoring_df)

feature_df = pd.DataFrame(feature_results)
# Align column names with dashboard expectations
feature_df = feature_df.rename(columns={"PSI": "psi", "KL": "kl"})
feature_df["timestamp"] = timestamp

feature_metrics_path = baseline_dir / "feature_drift_metrics.csv"
if feature_metrics_path.exists():
    feature_df.to_csv(feature_metrics_path, mode="a", header=False, index=False)
else:
    feature_df.to_csv(feature_metrics_path, index=False)

# Shadow model comparison (simple synthetic shadow model using noisy main predictions)
print("Generating shadow model comparison metrics...")
X_monitor = monitoring_df.drop(columns=["fail"])
X_monitor_scaled = scaler.transform(X_monitor)
main_probs = model.predict_proba(X_monitor_scaled)[:, 1]

rng = np.random.default_rng(seed=42)
shadow_noise = rng.normal(loc=0.0, scale=0.02, size=main_probs.shape)
shadow_probs = np.clip(main_probs + shadow_noise, 0.0, 1.0)

shadow_df = pd.DataFrame(
    {
        "timestamp": [timestamp] * len(main_probs),
        "main_pred": main_probs,
        "shadow_pred": shadow_probs,
    }
)

shadow_metrics_path = baseline_dir / "shadow_model_predictions.csv"
shadow_df.to_csv(shadow_metrics_path, index=False)

print("✅ Metrics saved for dashboard.")
