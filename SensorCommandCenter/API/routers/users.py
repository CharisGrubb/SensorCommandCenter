from fastapi import APIRouter

router = APIRouter()


@router.get("/users/{user_id}", tags=["users"])
async def get_details_details(user_id:str): ###User_ID should be a UUID
    return [{"User Role":"TEST"}]