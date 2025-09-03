from fastapi import FastAPI, HTTPException
from starlette.responses import PlainTextResponse, JSONResponse
from models import Characteristic

app = FastAPI(
    title="STD23002",
    description="This is a specification of STD23002"
)


cars_characteristics = []

@app.get("/ping")
def ping():
    return PlainTextResponse("pong")

@app.post("/cars", status_code=201)
def create_car(characteristic: Characteristic):
    cars_characteristics.append(characteristic)
    return characteristic

@app.get("/cars")
def get_all_cars():
    return cars_characteristics

@app.get("/cars/{id}")
def get_car_by_id(id: str):
    car = next((car for car in cars_characteristics if car.id == id), None)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@app.put("/cars/{id}/characteristics")
def update_car_characteristics(id: str, max_speed: float, max_fuel_capacity: float):
    car = next((car for car in cars_characteristics if car.id == id), None)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    car.max_speed = max_speed
    car.max_fuel_capacity = max_fuel_capacity
    return car
