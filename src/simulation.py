import numpy as np

def simulate_disease_rate(disease_rate, size=1000, seed=42):
    """
    Simulate proportion of disease using a binomial distribution.
    """
    np.random.seed(seed)
    simulated = np.random.binomial(1, disease_rate, size=size)
    return simulated.mean()
