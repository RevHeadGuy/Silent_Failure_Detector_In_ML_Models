import numpy as np
import joblib

def save_baseline_behavior(model, scaler, baseline_df):
    X = baseline_df.drop(columns=["fail"])
    X_scaled = scaler.transform(X)

    probs = model.predict_proba(X_scaled)[:, 1]

    baseline_stats = {
        "mean_probability": float(probs.mean()),
        "std_probability": float(probs.std()),
        "min_probability": float(probs.min()),
        "max_probability": float(probs.max()),
        "quantiles": {
            "25%": float(np.percentile(probs, 25)),
            "50%": float(np.percentile(probs, 50)),
            "75%": float(np.percentile(probs, 75)),
        }
    }

    joblib.dump(baseline_stats, "baseline/prediction_baseline.pkl")