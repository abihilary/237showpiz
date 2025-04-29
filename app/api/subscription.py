from fastapi import APIRouter

router = APIRouter()

# Simple example route
@router.get("/")
def subscribe_user():
    return {"message": "User subscribed successfully!"}
