from fastapi import APIRouter

router = APIRouter()

# Simple example route
@router.get("/")
def send_notification():
    return {"message": "Notification sent successfully!"}
