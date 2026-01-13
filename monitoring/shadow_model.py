import numpy as np

def model_disagreement(probs_old, probs_new):
    return np.mean(np.abs(probs_old - probs_new))