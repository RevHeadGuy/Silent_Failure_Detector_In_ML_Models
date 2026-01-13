import numpy as np

def prediction_entropy(probs):
    eps = 1e-6
    entropy = - (probs * np.log(probs + eps) +
                 (1 - probs) * np.log(1 - probs + eps))
    return entropy.mean()