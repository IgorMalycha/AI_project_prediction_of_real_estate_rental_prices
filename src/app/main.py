from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
import os

MODEL_PATH = "../data/reporting/best_model.pkl"

app = FastAPI(title="AI Model API", version="1.0")

# Wczytanie modelu
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Brak modelu: data/reporting/best_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


# --- Model danych wejściowych ---
class InputData(BaseModel):
    city: str
    type: str
    squareMeters: float
    rooms: float
    floor: float
    floorCount: float
    buildYear: float | None
    latitude: float
    longitude: float
    centreDistance: float
    poiCount: float
    schoolDistance: float
    clinicDistance: float
    postOfficeDistance: float
    kindergartenDistance: float
    restaurantDistance: float
    collegeDistance: float
    pharmacyDistance: float
    ownership: str
    buildingMaterial: str
    condition: str | None
    hasParkingSpace: str
    hasBalcony: str
    hasElevator: str
    hasSecurity: str
    hasStorageRoom: str


@app.get("/")
def home():
    return {"message": "Model API działa poprawnie 🚀"}


@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.dict()])

    try:
        pred = model.predict(df)
        value = float(pred[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Błąd predykcji: {e}")

    return {"prediction": value}
