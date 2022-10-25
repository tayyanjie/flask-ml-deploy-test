''' Test Flask App '''
import os
from app import app

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_index_route():
    """ Tests that home page works """
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Upload your CSV file" in response.data

def test_upload_form():
    """ Tests uploading of csv file for predictions """
    file = open(os.path.join(dir_path, "test_data.csv"), "rb") # pylint: disable=consider-using-with
    response = app.test_client().post("/",
            data={"file": file})
    assert response.status_code == 200
    assert response.headers["Content-Disposition"] == "attachment;filename=predictions.csv"
    assert response.headers["Content-Type"] == "text/csv"
