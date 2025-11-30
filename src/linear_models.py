import numpy as np
from sklearn.linear_model import LinearRegression

class HealthLinearModels:
    """
    Perform linear regression analyses on health study data.
    """
    def __init__(self, df):
        self.df = df

    def linear_regression_bp(self):
        """
        Predict systolic blood pressure from age and weight using linear regression.

        Returns
        -------
        model : sklearn.linear_model.LinearRegression
            Fitted regression model.
        dict : 
            Dictionary with 'intercept', 'coefficients', and predictions for first 5 rows.
        """
        X = self.df[['age', 'weight']].values
        y = self.df['systolic_bp'].values

        model = LinearRegression()
        model.fit(X, y)

        y_pred = model.predict(X[:5])

        return model, {
            "intercept": model.intercept_,
            "coefficients": model.coef_,
            "pred_first_5": y_pred.round(2)
        }

