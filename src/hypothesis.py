import numpy as np
from scipy.stats import norm
from scipy.stats import ttest_ind

def ci_normal(data, confidence=0.95):
    """
    Compute the confidence interval for the mean using normal approximation.

    Parameters
    ----------
    data : array-like
        Sample values.
    confidence : float, optional
        Confidence level (default 0.95).

    Returns
    -------
    (float, float)
        Lower and upper bounds of the confidence interval.
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
    Bootstrap confidence interval for the mean.

    Parameters
    ----------
    data : array-like
    B : int, number of resamples
    confidence : float, confidence level
    seed : int, random seed

    Returns
    -------
    (float, float) : lower and upper bounds
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


def bootstrap_ttest_smoking(df, bp_col="systolic_bp", smoker_col="smoker", n_boot=10000):
    """
    Performs a one-sided bootstrap hypothesis test:
    H0: mean_smokers <= mean_non_smokers
    H1: mean_smokers > mean_non_smokers
    Returns observed difference, p-value, and CI for difference.
    """

    smokers = df[df[smoker_col] == 'Yes'][bp_col].values
    non_smokers = df[df[smoker_col] == 'No'][bp_col].values

    np.random.seed(0)

    # Observed difference
    obs_diff = smokers.mean() - non_smokers.mean()

    # Bootstrap sampling distribution
    boot_diff = np.empty(n_boot)

    for i in range(n_boot):
        smokers_boot = np.random.choice(smokers, size=len(smokers), replace=True)
        non_smokers_boot = np.random.choice(non_smokers, size=len(non_smokers), replace=True)
        boot_diff[i] = smokers_boot.mean() - non_smokers_boot.mean()

    # One-sided p-value
    p_value = np.mean(boot_diff >= obs_diff)

    # Confidence interval
    ci_low, ci_high = np.percentile(boot_diff, [2.5, 97.5])

    return {
        "obs_diff": obs_diff,
        "p_value": p_value,
        "ci_low": ci_low,
        "ci_high": ci_high
    }


