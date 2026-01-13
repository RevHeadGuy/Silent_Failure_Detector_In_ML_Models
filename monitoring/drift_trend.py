import numpy as np

def compute_drift_trend(drift_history):
    x = np.arange(len(drift_history))
    slope = np.polyfit(x, drift_history, 1)[0]
    moving_avg = np.mean(drift_history[-3:])
    return {
        "slope": slope,
        "moving_avg": moving_avg
    }