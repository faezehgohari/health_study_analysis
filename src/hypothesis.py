import numpy as np
from scipy.stats import norm

def ci_normal(data, confidence=0.95):
    """
    Confidence interval using normal approximation.
    """
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    n = len(data)
    
    z = norm.ppf(1 - (1 - confidence) / 2)
    
    ci_low = mean - z * (std / np.sqrt(n))
    ci_high = mean + z * (std / np.sqrt(n))
    
    return ci_low, ci_high

def ci_bootstrap(data, B=5000, confidence=0.95, seed=42):
    """
    Confidence interval using bootstrap resampling.
    """
    np.random.seed(seed)
    boot_means = []
    n = len(data)

    for _ in range(B):
        sample = np.random.choice(data, size=n, replace=True)
        boot_means.append(sample.mean())

    alpha = (1 - confidence) * 100 / 2
    ci_low = np.percentile(boot_means, alpha)
    ci_high = np.percentile(boot_means, 100 - alpha)

    return ci_low, ci_high
