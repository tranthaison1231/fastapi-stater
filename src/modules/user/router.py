from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_users():
    return {"message": "Get all users"}
