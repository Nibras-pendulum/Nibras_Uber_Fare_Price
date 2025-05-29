from pydantic import BaseModel

class TripInput(BaseModel):
    pickup_latitude: float
    pickup_longitude: float
    dropoff_latitude: float
    dropoff_longitude: float
    timestamp: str

