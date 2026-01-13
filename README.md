# 🔍 Silent Failure Detector

A production-style machine learning monitoring system designed to detect silent failures in ML models by tracking prediction drift, feature drift, and behavioral degradation over time — without relying on immediate labels.

The system combines statistical drift detection, severity classification, alerting, and an interactive dashboard to ensure long-term model reliability.

# 🚀 Key Capabilities

1. Prediction Drift Detection

2. Detects changes in model prediction behavior using distribution-based metrics

3. Feature-Level Drift Monitoring

4. Tracks individual feature drift using PSI (Population Stability Index) and KL Divergence

5. Shadow Model Comparison

6. Compares production model predictions with a shadow model to approximate concept drift

7. Interactive Monitoring Dashboard

8. Streamlit dashboard with rolling window analysis and visualizations

9. Alert Routing System

10. Configurable alerting based on drift severity (console, email, Slack)

11. Severity Classification

Automatic classification of drift severity: LOW, MEDIUM, HIGH

Baseline Behavior Management

Captures and stores healthy baseline behavior for future comparisons
