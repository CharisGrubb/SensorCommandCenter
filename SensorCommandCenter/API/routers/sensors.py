from SensorCommandCenter.Auth.Authentication import AuthHandler
from SensorCommandCenter.Database.Database_Interfaces import InternalDBConnection
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
auth_handler = AuthHandler()

@router.get("/sensors", tags=["sensors"])
async def get_sensor_list(username: Annotated[str,Depends(auth_handler.authenticate_user)]):
    
    #Check Access Level
    auth_handler.check_user_access(access_required='R') #Check for read status

    if username is None:
        raise HTTPException(status_code = 401, detail='Unauthorized')
    else:
        try:
            db = InternalDBConnection()
            sensors = db.get_all_sensors()
           
            return {"results" : sensors}
        except:
            #Log error to database with traceback details
            print(traceback.format_exc())
            raise HTTPException(status_code=500, detail="Error occured. Contact administrator.")

    


@router.get("/sensor/{sensor_id}", tags=["sensors"])
async def get_sensor_details(sensor_id:str): ###Sensor_ID should be a UUID

    #Authenticate User

    return [{"Sensor Type":"TEST"}]

#PUT to UPDATE, POST to CREATE
@router.post("/sensor")
async def create_sensor(sensor:Sensor,username: Annotated[str | None, Header()] = None, password: Annotated[str | None, Header()] = None):
    if username is None:
        raise HTTPException(status_code = 401, details= 'Unauthorized')

    #DB CALL TO CREATE SENSOR

    #RETURN NEW SENSOR OBJECT
    return sensor

#PATHS are created in order; users/me before users/{user_ID} to avoid pydantic validation errors