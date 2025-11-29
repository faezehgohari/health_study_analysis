def calculate_basic_stats(df):
    '''
    Calculate basic descriptive statistics for selected columns.
    '''
    cols = ["age", "weight", "height", "systolic_bp", "cholesterol"]
    return df[cols].agg(["mean", "median", "min", "max"]).round(2)
