from fastapi import APIRouter, Depends, Header, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Annotated


import uuid
import secrets
import traceback

###AUTHORIZATION
security = HTTPBasic()
def get_current_username(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    print('Inside get username ')
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"JediMaster"
    is_correct_username = secrets.compare_digest(current_username_bytes, correct_username_bytes)

    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"R2D2_for_President"
    is_correct_password = secrets.compare_digest(current_password_bytes, correct_password_bytes)

    if not(is_correct_username and is_correct_password):
        raise HTTPException(status_code=401,detail="Incorrect username or password.", headers={"WWWAuthenticate":"Basic"})
    
    return credentials.username

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

#used for remote web/desktop log in
@router.post("/users/AuthUser", tags=["users"])
async def authenticate_user(username: Annotated[str | None, Header()] = None, password: Annotated[str | None, Header()] = None): 


    return [{"User Role":"TEST"}]