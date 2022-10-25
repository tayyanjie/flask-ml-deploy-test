from app import app
import pytest
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Upload your CSV file" in response.data

def test_upload_form():
    f = open(os.path.join(dir_path, "test_data.csv"), "rb")
    response = app.test_client().post("/",
            data={"file": f})
    assert response.status_code == 200
    assert response.headers["Content-Disposition"] == "attachment;filename=predictions.csv"
    assert response.headers["Content-Type"] == "text/csv"
