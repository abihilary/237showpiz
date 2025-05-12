import os

import uvicorn
from fastapi import FastAPI
from app.api import subscription, notification, comments, subscriber_routes, likes_route


app = FastAPI()

# Include your subscription and notification routes
app.include_router(subscription.router, prefix="/subscriptions")
app.include_router(notification.router, prefix="/notifications")
app.include_router(comments.router, prefix="/comments")
app.include_router(subscriber_routes.router, prefix="/subscribers")
app.include_router(likes_route.router, prefix="/likes", tags=["Likes"])


@app.get("/")
def root():
    return {"message": "Welcome to Showbiz Backend"}


# Run the app on 0.0.0.0 with dynamic port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
