from Database.Database_Interfaces import InternalDBConnection
from fastapi import APIRouter
from pydantic import BaseModel

############################################# API MODEL DEFINITIONS ##############################################################################
class Sensor(BaseModel):
    sensor_id: str
    sensor_type: str 
    sensor_model: str



############################################# API ENDPOINT DEFINITION ###################################################################

router = APIRouter()

@router.get("/sensors", tags=["sensors"])
async def get_sensor_list():
    db = InternalDBConnection()
    db.connect()
    sensors = db.get_all_sensors()
    db.close_connection()
    return {"results" : sensors}

    # return [{"Sensor Type": "Shelly", "Last Reading":"2024-09-06 11:53:02"},{"Sensor Type":"Manual","Last Reading": None}]


@router.get("/sensor/{sensor_id}", tags=["sensors"])
async def get_sensor_details(sensor_id:str): ###Sensor_ID should be a UUID
    return [{"Sensor Type":"TEST"}]

#PUT to UPDATE, POST to CREATE
@router.post("/sensor")
async def create_sensor(sensor:Sensor):
    #AUTHENTICATE USER

    #DB CALL TO CREATE SENSOR

    #RETURN NEW SENSOR OBJECT
    return sensor

#PATHS are created in order; users/me before users/{user_ID} to avoid pydantic validation errors