# 🔍 Silent Failure Detector

A production-style machine learning monitoring system designed to detect silent failures in ML models by tracking prediction drift, feature drift, and behavioral degradation over time — without relying on immediate labels.

The system combines statistical drift detection, severity classification, alerting, and an interactive dashboard to ensure long-term model reliability.

# 🚀 Key Capabilities

1. Prediction Drift Detection : Detects changes in model prediction behavior using distribution-based metrics

2. Feature-Level Drift Monitoring : Tracks individual feature drift using PSI (Population Stability Index) and KL Divergence

3. Shadow Model Comparison : Compares production model predictions with a shadow model to approximate concept drift

4. Interactive Monitoring Dashboard : Streamlit dashboard with rolling window analysis and visualizations

5. Alert Routing System : Configurable alerting based on drift severity (console, email, Slack)

6. Severity Classification : Automatic classification of drift severity: LOW, MEDIUM, HIGH

7. Baseline Behavior Management : Captures and stores healthy baseline behavior for future comparisons

# 🧠 Why Silent Failure Detection?

Traditional ML systems often fail silently:

1. The model keeps running

2. No exceptions are thrown

3. Predictions slowly become unreliable

This project detects those failures early, before accuracy drops or business impact occurs.

# ⚙️ Installation

Prerequisites

Python 3.8+

pip or conda

Setup

git clone <repository-url>

cd silent_failure_detector

pip install -r requirements.txt

requirements.txt

pandas>=1.5.0

numpy>=1.23.0

scikit-learn>=1.2.0

streamlit>=1.25.0

joblib>=1.2.0

pyyaml>=6.0

scipy>=1.10.0

plotly>=5.15.0

▶️ Usage

1️⃣ Run the Monitoring Pipeline

python main.py

This will:

1. Load and split the dataset into baseline (60%) and monitoring (40%)

2. Train a logistic regression model

3. Save baseline prediction behavior

4. Compute prediction drift metrics

5. Detect feature-level drift (PSI + KL)

6. Perform shadow model comparison

7. Save all outputs to the baseline/ directory

2️⃣ Launch the Dashboard

streamlit run dashboard/app.py

The dashboard provides:

1. Overall drift severity

2. Prediction drift trends (rolling windows)

3. Feature-level root cause analysis

4. Shadow model disagreement analysis

5. Alert summaries and recommendations
