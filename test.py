import joblib
import pandas as pd


def test_logistic_1():
    model = joblib.load("models/LogisticRegressionModel.joblib")
    data = pd.read_csv("data/test_data.csv")
    model.predict(data)
