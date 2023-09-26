from fastapi.testclient import TestClient
from fastapi import status
from main import app

# Initiate test client with the app instance for unit testing
client = TestClient(app)

''' Unit testing for Health Check API endpoint '''
def test_health_check_endpoint():
    response = client.get("/health_check")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "UP"}

''' Unit testing for Get Features API endpoint '''
# Read the JSON data from the test file
with open("test_data.json", "r") as json_file:
    test_json_data = json_file.read()

def test_get_features_endpoint():
    data = {"data":[{"customer_ID": "123", "loans": [{"customer_ID": "123", "loan_date": "2022-01-01", "amount": 1000}]}]}
    response = client.post("/get_features", files={"file": ("test_data.json", test_json_data)})
    assert response.status_code == 200
    #assert "features_extracted" in response.json()