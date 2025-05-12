# models/comment.py
from pydantic import BaseModel
from datetime import datetime


class Comment(BaseModel):
    text: str
    subscriber_id: str
    comment_count: int = None
    timestamp: datetime = None
    post_id: str = None
