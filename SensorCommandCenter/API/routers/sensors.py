from Database.Database_Interfaces import InternalDBConnection
from fastapi import APIRouter, Depends, Header, HTTPException

from pydantic import BaseModel
from typing import Annotated

import traceback
import secrets

############################################# API MODEL DEFINITIONS ##############################################################################
class Sensor(BaseModel):
    sensor_id: str
    sensor_type: str 
    sensor_model: str



############################################# API ENDPOINT DEFINITION ###################################################################

router = APIRouter()

@router.get("/sensors", tags=["sensors"])
async def get_sensor_list(username: Annotated[str | None, Header()] = None, password: Annotated[str | None, Header()] = None):
    #Authenticate User first
    if username is None:
        raise HTTPException(status_code = 401, detail='Unauthorized')
    else:
        try:
            db = InternalDBConnection()
            db.connect()
            sensors = db.get_all_sensors()
            db.close_connection()
            return {"results" : sensors}
        except:
            #Log error to database with traceback details
            raise HTTPException(status_code=500, detail="Error occured. Contact administrator.")

    


@router.get("/sensor/{sensor_id}", tags=["sensors"])
async def get_sensor_details(sensor_id:str): ###Sensor_ID should be a UUID

    #Authenticate User

    return [{"Sensor Type":"TEST"}]

#PUT to UPDATE, POST to CREATE
@router.post("/sensor")
async def create_sensor(sensor:Sensor):
    #AUTHENTICATE USER

    #DB CALL TO CREATE SENSOR

    #RETURN NEW SENSOR OBJECT
    return sensor

#PATHS are created in order; users/me before users/{user_ID} to avoid pydantic validation errors