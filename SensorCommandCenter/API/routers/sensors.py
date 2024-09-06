from fastapi import APIRouter

router = APIRouter()


@router.get("/sensors", tags=["sensors"])
async def get_sensor_list():
    return [{"Sesnor Type": "Shelly", "Last Reading":"2024-09-06 11:53:02"},{"Sensor Type":"Manual","Last Reading": None}]


@router.get("/sensor/{sensor_id}", tags=["sensors"])
async def get_sensor_details(sensor_id:str): ###Sensor_ID should be a UUID
    return [{"Sensor Type":"TEST"}]