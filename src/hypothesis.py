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
import numpy as np
from scipy.stats import ttest_ind

def one_sided_ttest_smoking(df, bp_col="systolic_bp", smoker_col="smoker"):
    """
    Performs a one-sided t-test where the hypothesis is:
    H0: mean_smokers <= mean_non_smokers
    H1: mean_smokers > mean_non_smokers
    """

    smokers = df[df[smoker_col] == 'Yes'][bp_col]
    non_smokers = df[df[smoker_col] == 'No'][bp_col]

    t_stat, p_value = ttest_ind(smokers, non_smokers, alternative='greater')

    results = {
        "mean_smokers": smokers.mean(),
        "mean_non_smokers": non_smokers.mean(),
        "t_stat": t_stat,
        "p_value": p_value
    }

    return results

