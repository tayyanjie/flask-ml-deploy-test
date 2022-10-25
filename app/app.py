'''
Flask app to allow for upload of csv to generate predictions returned in CSV format.
'''
import os
import joblib
import pandas as pd
from flask import Flask, request, make_response, render_template



app = Flask(__name__)
path = os.path.dirname(os.path.realpath(__file__))
model = joblib.load(os.path.join(path, "../models/LogisticRegressionModel.joblib"))


@app.route("/")
def form():
    """Generates Form to upload csv for prediction"""
    return render_template("index.html")


@app.route("/", methods=["POST"])
def predict():
    """Conduct prediction and allow for download of resulting CSV"""
    file = request.files.get("file")
    data = pd.read_csv(file)
    res = model.predict(data)
    data["label"] = res
    resp = make_response(data.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment;filename=predictions.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp


if __name__ == "__main__":
    app.run(debug=True)
