import numpy as np

def psi(expected, actual, buckets=10):
    expected, actual = expected.dropna(), actual.dropna()
    breaks = np.percentile(expected, np.linspace(0, 100, buckets + 1))

    exp_counts, _ = np.histogram(expected, breaks)
    act_counts, _ = np.histogram(actual, breaks)

    exp_pct = exp_counts / exp_counts.sum()
    act_pct = act_counts / act_counts.sum()

    return np.sum((act_pct - exp_pct) * np.log(act_pct / exp_pct))

