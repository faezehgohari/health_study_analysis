# linear_models.py
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def linear_regression_bp(df):
    """
    Enkel linjär regression för att förutsäga systoliskt blodtryck
    från ålder och vikt.
    """
    X = df[['age', 'weight']].values
    y = df['systolic_bp'].values

    model = LinearRegression()
    model.fit(X, y)

    # Print resultat med förklaring
    print("Intercept:", model.intercept_)
    print("Coefficients (age, weight):", model.coef_)
    
    y_pred = model.predict(X[:5])
    print("Predictions for first 5 individuals:", y_pred.round(2))

    return model, y_pred
