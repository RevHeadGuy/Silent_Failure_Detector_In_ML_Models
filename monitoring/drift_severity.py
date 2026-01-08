def classify_prediction_drift(drift_metrics, thresholds):
    severity = "LOW"

    for metric, value in drift_metrics.items():
        if value > thresholds.get(metric, float("inf")):
            severity = "HIGH"

    return severity