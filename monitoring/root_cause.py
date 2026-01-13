def rank_drift_causes(psi, importance, trend):
    scores = {}
    for feature in psi:
        scores[feature] = psi[feature] * importance.get(feature, 1) * trend
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)