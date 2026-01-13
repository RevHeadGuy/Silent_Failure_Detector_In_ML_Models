import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
import sys

# Ensure project root is on sys.path so we can import top-level packages like `alerts`
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from layout import render_title, render_metric, render_section, render_expander
from charts import plot_drift_line_chart, plot_feature_bar_chart
from alerts.alert_router import route_alert  # Feature 8: Alert routing

# -----------------------------
# Load CSS for styling (relative to this file)
# -----------------------------
css_path = ROOT_DIR / "dashboard" / "style.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Dashboard Header
# -----------------------------
render_title("Silent Failure Monitoring Dashboard")

# -----------------------------
# Load drift results
# -----------------------------
drift_metrics_file = "baseline/prediction_drift_metrics.csv"
feature_drift_file = "baseline/feature_drift_metrics.csv"
shadow_model_file = "baseline/shadow_model_predictions.csv"  # shadow model comparison

try:
    drift_df = pd.read_csv(drift_metrics_file, parse_dates=["timestamp"])
    feature_df = pd.read_csv(feature_drift_file)
    shadow_df = pd.read_csv(shadow_model_file, parse_dates=["timestamp"])
except FileNotFoundError:
    st.warning("Drift or shadow model metrics not found. Run main.py first!")
    st.stop()

# -----------------------------
# Rolling Window Selection
# -----------------------------
window_option = st.selectbox("Select Rolling Window", ["Last 1 hour", "Last 1 day", "Last 7 days"])
now = drift_df['timestamp'].max()

if window_option == "Last 1 hour":
    start_time = now - timedelta(hours=1)
elif window_option == "Last 1 day":
    start_time = now - timedelta(days=1)
else:
    start_time = now - timedelta(days=7)

rolling_df = drift_df[drift_df['timestamp'] >= start_time]

# -----------------------------
# Overall Metrics (Latest)
# -----------------------------
latest_drift = rolling_df.iloc[-1]
severity_map = {"LOW": "healthy", "MEDIUM": "warning", "HIGH": "critical"}

render_section("Overall Drift Summary")
render_metric("Drift Severity", latest_drift['severity'], severity=severity_map[latest_drift['severity']])
render_metric("Mean Shift", round(latest_drift['mean_shift'], 4))
render_metric("Std Shift", round(latest_drift['std_shift'], 4))
render_metric("Distribution Distance", round(latest_drift['distribution_distance'], 4))

# -----------------------------
# Prediction Drift Trends
# -----------------------------
render_section("Prediction Drift Trends (Rolling Window)")
plot_drift_line_chart(rolling_df, metric_name="mean_shift")
plot_drift_line_chart(rolling_df, metric_name="std_shift")
plot_drift_line_chart(rolling_df, metric_name="distribution_distance")

# -----------------------------
# Feature-Level Drift
# -----------------------------
render_section("Feature-Level Drift Analysis")
feature_df['severity'] = feature_df['psi'].apply(
    lambda x: "HIGH" if x>=0.3 else ("MEDIUM" if x>=0.2 else ("LOW" if x>=0.1 else "NORMAL"))
)
plot_feature_bar_chart(feature_df)

# -----------------------------
# Shadow Model Comparison
# -----------------------------
render_section("Shadow Model Comparison")
shadow_df['disagreement'] = abs(shadow_df['main_pred'] - shadow_df['shadow_pred'])
disagreement_rate = shadow_df['disagreement'].mean()
render_metric("Shadow Model Disagreement Rate", f"{disagreement_rate*100:.2f}%", 
              severity="warning" if disagreement_rate>0.2 else "healthy")

# Optional: plot disagreement trend
plot_drift_line_chart(shadow_df.rename(columns={'disagreement': 'distribution_distance'}), metric_name='distribution_distance')

# -----------------------------
# Alerts & Recommendations
# -----------------------------
render_section("Alerts & Recommendations")

def generate_alert_message(row):
    if row['severity'] == "HIGH":
        return f"🚨 HIGH drift alert for {row['feature']} | PSI={row['psi']:.3f} | KL={row['kl']:.3f}"
    elif row['severity'] == "MEDIUM":
        return f"⚠️ Medium drift for {row['feature']} | PSI={row['psi']:.3f} | KL={row['kl']:.3f}"
    else:
        return None

feature_df['alert_message'] = feature_df.apply(generate_alert_message, axis=1)
alert_rows = feature_df.dropna(subset=['alert_message'])

if len(alert_rows) == 0:
    st.success("✅ All features are within normal ranges")
else:
    for _, row in alert_rows.iterrows():
        alert_msg = row['alert_message']
        st.warning(alert_msg)
        # -----------------------------
        # Route alerts based on severity
        # -----------------------------
        row_severity = row['severity']
        route_alert(row_severity, alert_msg)  # sends to console/email/Slack (stubbed)

# -----------------------------
# Last Monitoring Run
# -----------------------------
last_run = drift_df['timestamp'].max()
st.markdown(f"**Last Monitoring Run:** {last_run}")
