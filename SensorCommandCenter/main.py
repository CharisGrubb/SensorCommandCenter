from fastapi import FastAPI
from API.routers import sensors

app = FastAPI()


app.include_router(sensors.router)