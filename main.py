from monitoring.prediction_drift import compute_prediction_drift
from monitoring.drift_severity import classify_prediction_drift
from config.thresholds import PREDICTION_DRIFT_THRESHOLDS
from src.load_data import load_dataset, split_baseline_monitoring
from model.train_model import train_model
from baseline.save_baseline_predictions import save_baseline_behavior

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

severity = classify_prediction_drift(
    pred_drift, PREDICTION_DRIFT_THRESHOLDS
)

print("Prediction Drift Metrics:", pred_drift)
print("⚠️ Drift Severity:", severity)
