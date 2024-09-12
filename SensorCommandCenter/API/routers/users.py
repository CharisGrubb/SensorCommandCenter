from fastapi import APIRouter
from pydantic import BaseModel

import uuid



#################MODELS#################
class User(BaseModel):
    user_id: str | None = uuid.uuid4()
    username: str
    f_name: str
    l_name: str 
    e_mail: str | None = None 
    role: str | None = "Standard User"


####################### ENDPOINTS ###########################

router = APIRouter()
@router.get("/users/{user_id}", tags=["users"])
async def get_user_details(user_id:str): ###User_ID should be a UUID
    return [{"User Role":"TEST"}]

@router.put("/users/{user_id}", tags=["users"])
async def update_user_details(user_id:str, user:User): ###User_ID should be a UUID
    return [{"User Role":"TEST"}]

@router.post("/users/newUser", tags=["users"])
async def create_user_details(user:User): 
    return [{"User Role":"TEST"}]