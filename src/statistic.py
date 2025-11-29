import pandas as pd

def calculate_basic_stats(df):
    '''
    Calculate basic descriptive statistics for selected columns.
    '''
    cols = ["age", "weight", "height", "systolic_bp", "cholesterol"]
    return df[cols].agg(["mean", "median", "min", "max"]).round(2)

def calculate_disease_rate(df):
    """
    Beräknar andelen personer med sjukdom i procent.
    """
    rate = df["disease"].value_counts(normalize=True)[1]
    return rate, rate * 100

def compare_ci(ci_normal, ci_bootstrap):
    """
    Creates a comparison table for two confidence intervals.
    """
    ci_norm_low, ci_norm_high = ci_normal
    ci_boot_low, ci_boot_high = ci_bootstrap

    ci_table = pd.DataFrame({
        "Low": [ci_norm_low, ci_boot_low],
        "High": [ci_norm_high, ci_boot_high]
    }, index=["Normal", "Bootstrap"])

    return ci_table.round(3)