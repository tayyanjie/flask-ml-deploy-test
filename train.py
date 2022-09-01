import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

data = pd.read_csv("data/heart_failure_clinical_records_dataset.csv")
print("Loaded Data")

categorical_features = ["anaemia", "diabetes", "high_blood_pressure", "smoking", "sex"]
y = "DEATH_EVENT"
numerical_features = [
    feature
    for feature in data.columns
    if feature not in categorical_features and feature != y
]

y_train = data.DEATH_EVENT
x_train = data.drop("DEATH_EVENT", axis=1)


def create_pipeline(model):
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")
    numeric_transformer = StandardScaler()
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numerical_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )
    clf = Pipeline(steps=[("preprocessor", preprocessor), ("classifier", model)])
    return clf


pipeline = create_pipeline(LogisticRegression())

pipeline.fit(x_train, y_train)
print("Model Fitted")

model_path = "models/LogisticRegressionModel.joblib"
joblib.dump(pipeline, model_path)
print(f"Model saved at {model_path}")
