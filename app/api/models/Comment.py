# models/comment.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid


class Comment(BaseModel):
    comment_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    text: str
    subscriber_id: str
    comment_count: Optional[int] = None
    timestamp: Optional[datetime] = None
    post_id: Optional[str] = None
