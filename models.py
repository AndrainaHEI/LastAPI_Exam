from pydantic import BaseModel

class Characteristic(BaseModel):
    id: str
    brand: str
    model: str
    max_speed: float
    max_fuel_capacity: float