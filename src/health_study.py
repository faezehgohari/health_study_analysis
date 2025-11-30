import pandas as pd


class HealthStudyAnalizer:
    """
    A class for managing and cleaning health study data.

    Attributes
    ----------
    df : pandas.DataFrame
        The input dataset containing health-related variables such as sex, smoker status, and disease.
    """
    def __init__(self, df):
        """
        Initializes the HealthStudyAnalizer with a DataFrame.

        Parameters
        ----------
        df : pandas.DataFrame
            The health dataset to be analyzed and cleaned.
        """
        self.df = df

    def clean_df(self):
        """
        Cleans the DataFrame by standardizing column names and converting selected columns to categorical.

        Operations performed:
        - Strips whitespace from column names
        - Replaces spaces in column names with underscores
        - Converts all column names to lowercase
        - Converts 'sex', 'smoker', and 'disease' columns to pandas 'category' dtype

        Returns
        -------
        pandas.DataFrame
            The cleaned DataFrame ready for analysis.
        """
        self.df = self.df.copy()
        self.df.columns = self.df.columns.str.strip().str.replace(" ", "_").str.lower()
        for col in ["sex", "smoker", "disease"]:
            self.df[col] = self.df[col].astype("category")
        return self.df
