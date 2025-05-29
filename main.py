from fastapi import FastAPI
from schemas import TripInput
from predict import predict_fare
from xgboost import XGBRegressor

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Uber Fare Prediction API"}

@app.post("/predict")
def get_prediction(trip: TripInput):
    fare = predict_fare(trip.dict())
    return {"predicted_fare": round(fare, 2)}
