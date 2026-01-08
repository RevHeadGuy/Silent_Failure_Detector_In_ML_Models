def classify_drift_severity(psi_value):
    if psi_value < 0.1:
        return "NORMAL"
    elif psi_value < 0.2:
        return "LOW"
    elif psi_value < 0.3:
        return "MEDIUM"
    else:
        return "HIGH"