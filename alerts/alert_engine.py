def generate_alert(feature_name, severity, psi, kl):
    if severity == "HIGH":
        return f"🚨 HIGH DRIFT ALERT | Feature: {feature_name} | PSI={psi} | KL={kl}"
    elif severity == "MEDIUM":
        return f"⚠️ MEDIUM DRIFT WARNING | Feature: {feature_name} | PSI={psi} | KL={kl}"
    else:
        return None