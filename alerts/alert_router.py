def route_alert(severity, message):
    if severity == "LOW":
        log_alert(message)
    elif severity == "MEDIUM":
        send_email(message)
    elif severity == "HIGH":
        send_slack(message)


def log_alert(message):
    print(f"[LOG] {message}")


def send_email(message):
    print(f"[EMAIL] {message}")


def send_slack(message):
    print(f"[SLACK] {message}")
