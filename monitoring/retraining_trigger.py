def check_retraining_needed(severity_history, threshold=3):
    recent = severity_history[-threshold:]
    if all(s == "HIGH" for s in recent):
        return True
    return False