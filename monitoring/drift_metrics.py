import numpy as np
import pandas as pd
from scipy.stats import entropy

def compute_kl_divergence(baseline, monitoring, bins = 10):
    baseline_hist, bin_edges = np.histogram(baseline, bins = bins, density = True)
    monitoring_hist, _ = np.histogram(monitoring, bins = bins, density = True)

    baseline_hist += 1e-10
    monitoring_hist += 1e-10

    return entropy(baseline_hist, monitoring_hist)

def compute_psi(baseline, monitoring, bins = 10):
    baseline_percents, bin_edges = np.histogram(baseline, bins = bins)
    monitoring_percents, _ = np.histogram(monitoring, bins = bins)

    baseline_percents = baseline_percents / len(baseline)
    monitoring_percents = monitoring_percents / len(monitoring)

    psi_value = np.sum((monitoring_percents - baseline_percents) * np.log((monitoring_percents + 1e-10) / (baseline_percents + 1e-10)))

    return psi_value