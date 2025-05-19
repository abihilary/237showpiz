from fastapi import APIRouter

from app.api.services.socket import ConnectionManager

manager = ConnectionManager()

router = APIRouter()


# Example endpoint to trigger a push notification
@router.post("/notify/")
async def notify_all_users(message: str):
    await manager.broadcast(message)
    return {"message": "Notification sent"}
