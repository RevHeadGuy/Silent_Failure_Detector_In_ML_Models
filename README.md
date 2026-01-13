# 🔍 Silent Failure Detector

A production-style machine learning monitoring system designed to detect silent failures in ML models by tracking prediction drift, feature drift, and behavioral degradation over time — without relying on immediate labels.

The system combines statistical drift detection, severity classification, alerting, and an interactive dashboard to ensure long-term model reliability.

# 🚀 Key Capabilities

Prediction Drift Detection

Detects changes in model prediction behavior using distribution-based metrics

Feature-Level Drift Monitoring

Tracks individual feature drift using PSI (Population Stability Index) and KL Divergence

Shadow Model Comparison

Compares production model predictions with a shadow model to approximate concept drift

Interactive Monitoring Dashboard

Streamlit dashboard with rolling window analysis and visualizations

Alert Routing System

Configurable alerting based on drift severity (console, email, Slack)

Severity Classification

Automatic classification of drift severity: LOW, MEDIUM, HIGH

Baseline Behavior Management

Captures and stores healthy baseline behavior for future comparisons
