from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "Model API" in response.text or "działa" in response.text


def test_predict():
    payload = {
  "city": "warszawa",
  "type": "apartmentbuilding",
  "squareMeters": 52.0,
  "rooms": 2.0,
  "floor": 3.0,
  "floorCount": 3.0,
  "buildYear": 2008.0,
  "latitude": 52.24,
  "longitude": 20.96,
  "centreDistance": 1.22,
  "poiCount": 18.0,
  "schoolDistance": 0.08,
  "clinicDistance": 0.14,
  "postOfficeDistance": 0.22,
  "kindergartenDistance": 0.24,
  "restaurantDistance": 0.06,
  "collegeDistance": 0.67,
  "pharmacyDistance": 0.12,
  "ownership": "condominium",
  "buildingMaterial": "brick",
  "condition": "premium",
  "hasParkingSpace": "yes",
  "hasBalcony": "yes",
  "hasElevator": "yes",
  "hasSecurity": "no",
  "hasStorageRoom": "no"
}

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    json_resp = response.json()
    assert "prediction" in json_resp
    assert isinstance(json_resp["prediction"], float)
