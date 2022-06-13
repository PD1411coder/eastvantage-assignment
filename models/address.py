from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip: str   
    lat: float
    lng: float
