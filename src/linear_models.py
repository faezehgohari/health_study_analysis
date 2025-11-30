import numpy as np
from sklearn.linear_model import LinearRegression

class HealthLinearModels:
    def __init__(self, df):
        self.df = df

    def linear_regression_bp(self):
        """
        Linjär regression för att förutsäga systoliskt blodtryck
        från ålder och vikt.
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

