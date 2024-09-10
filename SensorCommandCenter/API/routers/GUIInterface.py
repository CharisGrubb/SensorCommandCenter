from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root(theme: str = "Standard"): ###Home Web Page
    return {"message":"Hello World"}



@router.get("/UserManagement")
async def root(theme: str = "Standard"): ###Home Web Page
    return {"message":"UserManagement"}