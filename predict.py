import joblib
import pandas as pd

model = joblib.load("fare_prediction_model.pkl")

def predict_fare(trip_data: dict):
    df = pd.DataFrame([trip_data])
    return model.predict(df)[0]
