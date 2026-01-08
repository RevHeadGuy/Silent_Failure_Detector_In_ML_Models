from monitoring.drift_metrics import compute_kl_divergence, compute_psi
from monitoring.severity import classify_drift_severity
from alerts.alert_engine import generate_alert

EXCLUDED_COLS = ["fail"]

def monitor_features(baseline_df, monitoring_df):
    results = []
    alerts = []

    for col in baseline_df.columns:
        if col in EXCLUDED_COLS:
            continue

        baseline_col = baseline_df[col]
        monitoring_col = monitoring_df[col]

        kl = round(compute_kl_divergence(baseline_col, monitoring_col), 4)
        psi = round(compute_psi(baseline_col, monitoring_col), 4)

        severity = classify_drift_severity(psi)

        alert = generate_alert(col, severity, psi, kl)
        if alert:
            alerts.append(alert)

        results.append({
            "feature": col,
            "KL": kl,
            "PSI": psi,
            "severity": severity
        })

    return results, alerts
