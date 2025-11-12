import pandas as pd


class HealthStudyAnalizer:
    def __init__(self, df):
        self.df = df

    def clean_df(self):
        self.df = self.df.copy()
        self.df.columns = self.df.columns.str.strip().str.replace(" ", "_").str.lower()
        for col in ["sex", "smoker", "disease"]:
            self.df[col] = self.df[col].astype("category")
        return self.df
