import pandas as pd
import os

def load_data(path="../data/health_study_dataset.csv"):
    """
    Load the health study dataset from a CSV file.

    Parameters
    ----------
    path : str
        Path to the CSV file (default "../data/health_study_dataset.csv").

    Returns
    -------
    pandas.DataFrame
        The loaded dataset.
    """
    return pd.read_csv(path)