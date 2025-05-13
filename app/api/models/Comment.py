# models/comment.py
from typing import Optional

from pydantic import BaseModel
from datetime import datetime


class Comment(BaseModel):
    text: str
    subscriber_id: str
    comment_count: Optional[int] = None
    timestamp: Optional[datetime] = None
    post_id: Optional[str] = None
