import numpy as np
import joblib
from scipy.stats import wasserstein_distance

def compute_prediction_drift(model, scaler, monitoring_df):
    baseline_stats = joblib.load("baseline/prediction_baseline.pkl")

    X = monitoring_df.drop(columns=["fail"])
    X_scaled = scaler.transform(X)

    probs = model.predict_proba(X_scaled)[:, 1]

    drift_results = {}

    # Mean shift
    drift_results["mean_shift"] = abs(
        probs.mean() - baseline_stats["mean_probability"]
    )

    # Std deviation shift
    drift_results["std_shift"] = abs(
        probs.std() - baseline_stats["std_probability"]
    )

    # Distribution distance
    baseline_quantiles = np.array(
        list(baseline_stats["quantiles"].values())
    )
    current_quantiles = np.percentile(probs, [25, 50, 75])

    drift_results["distribution_distance"] = wasserstein_distance(
        baseline_quantiles, current_quantiles
    )

    return drift_results