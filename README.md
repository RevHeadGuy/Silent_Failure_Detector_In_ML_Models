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

⚙️ Installation

Prerequisites

Python 3.8+

pip or conda

Setup

git clone <repository-url>

cd silent_failure_detector

pip install -r requirements.txt
