import os

import uvicorn
from fastapi import WebSocket, WebSocketDisconnect
from fastapi import FastAPI
from app.api import subscription, notification, comments, subscriber_routes, likes_route,socket_rout
from app.api.socket_rout import manager

app = FastAPI()

# Include your subscription and notification routes
app.include_router(subscription.router, prefix="/subscriptions")
app.include_router(notification.router, prefix="/notifications")
app.include_router(comments.router, prefix="/comments")
app.include_router(subscriber_routes.router, prefix="/subscribers")
app.include_router(likes_route.router, prefix="/likes", tags=["Likes"])
app.include_router(socket_rout.router, prefix="/notify", tags=["notify"])


@app.get("/")
def root():
    return {"message": "Welcome to Showbiz Backend"}

@app.websocket("/ws/notifications")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Optional: echo or handle user input
            await manager.send_personal_message(f"Message received: {data}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)


# Run the app on 0.0.0.0 with dynamic port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
