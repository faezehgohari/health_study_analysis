import pandas as pd
import os

def load_data(path="../data/health_study_dataset.csv"):
    return pd.read_csv(path)