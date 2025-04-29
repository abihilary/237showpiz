import os

from fastapi import APIRouter, HTTPException
from app.api.models.Comment import Comment
from app.api.services import comment_service, subscriber_service
from datetime import datetime
from typing import List, Dict

from app.api.services.comment_service import get_subscriber_name

router = APIRouter()


@router.get("/", response_model=List[Comment])
def get_all_comments():
    return comment_service.load_all_comments()


@router.post("/")
def post_comment(comment: Comment):
    # Ensure subscriber exists
    if not subscriber_service.get_subscriber_by_id(comment.subscriber_id):
        raise HTTPException(status_code=404, detail="Subscriber not found")

    comment = Comment(
        text=comment.text,
        subscriber_id=comment.subscriber_id,
    )

    comment_service.add_comment(comment)
    return {"message": "Comment added successfully."}


@router.post("/batch")
def post_multiple_comments(comments: List[Comment]):
    # Check if all subscribers exist
    invalid = [c.subscriber_id for c in comments if not subscriber_service.get_subscriber_by_id(c.subscriber_id)]
    if invalid:
        raise HTTPException(status_code=404, detail=f"Subscribers not found: {invalid}")

    comment_service.add_comments_batch(comments)
    return {"message": f"{len(comments)} comments added successfully."}


@router.get("/{subscriber_id}", response_model=List[Dict])
def get_comments_by_subscriber(subscriber_id: str):
    # Check if subscriber exists  
    if not subscriber_service.get_subscriber_by_id(subscriber_id):
        raise HTTPException(status_code=404, detail="Subscriber not found")

    comments = comment_service.get_comments_by_subscriber(subscriber_id)
    response = []

    for comment in comments:
        name = get_subscriber_name(comment.subscriber_id)
        response.append({
            "text": comment.text,
            "timestamp": datetime.now(),
            "subscriber_id": comment.subscriber_id,
            "subscriber_name": name
        })

    return response
