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

