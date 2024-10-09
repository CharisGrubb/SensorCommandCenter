from fastapi import FastAPI
from API.routers import GUIInterface, sensors, users
app = FastAPI()


app.include_router(sensors.router) #API Endpoints for sensor data. Sensor services connect to this endpoint to push data or register sensors
app.include_router(GUIInterface.router) #API section used by the GUI desktop application, to pull themes and dashboard data
app.include_router(users.router) #API Endpoints to manage users 

