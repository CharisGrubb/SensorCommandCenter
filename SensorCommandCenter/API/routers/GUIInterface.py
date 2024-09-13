from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root(theme: str = "Standard"): ###Home Web Page
    return {"message":"Hello World"}



@router.get("/UserManagement")
async def userManagment(theme: str = "Standard"): ###Home Web Page
    return {"message":"UserManagement"}


@router.get("/UserManagement/{user_id}")
async def userManagment(user_id,theme: str = "Standard"): ###Home Web Page
    return {"message":"UserManagement"}