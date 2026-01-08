# Silent Failure Detector for ML Models

A modular system to detect silent failures in machine learning models by monitoring prediction drift (and optionally feature drift) between a historical baseline period and new monitoring data.

Silent failures occur when a model’s performance degrades without throwing errors—this project is designed to catch such issues early.

🚀 Key Idea

Instead of waiting for accuracy drops in production, this system:

Establishes a baseline behavior from historical data

Continuously compares current model predictions against that baseline

Flags drift severity when deviations exceed safe thresholds

📌 Core Concepts

Baseline period
Historical data used to define normal model behavior

Monitoring period
New incoming data checked against the baseline

Prediction drift
Changes in the distribution of model output probabilities

Feature drift (optional)
Changes in input feature distributions

Silent failures
Model degradation without explicit runtime errors

⚙️ Step-by-Step Workflow

Step 1: Configuration (src/config.py)

Defines core constants:

DATA_PATH – Path to input CSV file

BASELINE_RATIO – 0.6 (60% baseline, 40% monitoring)

TARGET_COL – "fail" (target variable)

Step 2: Data Loading (src/load_data.py)

load_dataset()
Loads the CSV into a pandas DataFrame

split_baseline_monitoring(df)
Splits data into:

Baseline (60%) – historical reference

Monitoring (40%) – new data for drift detection

Step 3: Model Training (model/train_model.py)

train_model(baseline_df):

Separates features (X) and target (y = "fail")

Standardizes features using StandardScaler

Trains a Logistic Regression classifier

Returns:

Trained model

Fitted scaler

Step 4: Baseline Establishment (baseline/save_baseline_predictions.py)

save_baseline_behavior(model, scaler, baseline_df):

Generates prediction probabilities on baseline data

Computes reference statistics:

Mean, standard deviation

Min, max

25th, 50th, 75th percentiles

Saves statistics to:

baseline/prediction_baseline.pkl


This file represents normal model behavior.

Step 5: Prediction Drift Detection (monitoring/prediction_drift.py)

compute_prediction_drift(model, scaler, monitoring_df):

Loads baseline statistics

Generates predictions on monitoring data

Computes drift metrics:

Mean shift – absolute difference in mean probabilities

Std shift – absolute difference in standard deviations

Distribution distance – Wasserstein distance between quantiles

Returns a dictionary of drift metrics

Step 6: Drift Severity Classification (monitoring/drift_severity.py)

classify_prediction_drift(drift_metrics, thresholds):

Compares drift metrics against thresholds from config/thresholds.py

Default thresholds:

mean_shift = 0.05
std_shift = 0.05
distribution_distance = 0.1


Outputs drift severity:

LOW

HIGH

Step 7: Feature-Level Monitoring (Optional)

(monitoring/feature_monitor.py)

monitor_features(baseline_df, monitoring_df):

For each feature (excluding target):

Computes KL divergence

Computes PSI (Population Stability Index)

Severity rules:

PSI < 0.1 → NORMAL

PSI < 0.2 → LOW

PSI < 0.3 → MEDIUM

PSI ≥ 0.3 → HIGH

Triggers alerts for MEDIUM / HIGH via alerts/alert_engine.py

⚠️ Feature monitoring is implemented but not called in main.py by default.

▶️ Main Execution Flow (main.py)

Load dataset from CSV

Split into baseline (60%) and monitoring (40%)

Train logistic regression model on baseline data

Save baseline prediction statistics

Compute prediction drift metrics on monitoring data

Classify drift severity (LOW / HIGH)

Print results to console

🧠 How It Detects Silent Failures

The system compares current prediction behavior against a historical baseline.
If prediction distributions shift significantly in terms of:

Mean

Variance

Overall distribution shape

…it flags a potential silent failure, allowing teams to react before production impact.

🔮 Future Extensions

Automated alerts (Slack / Email)

Continuous monitoring pipelines

Integration with CI/CD or MLOps tools

Model performance drift tracking

Dashboard visualization
