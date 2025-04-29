# models/comment.py
from pydantic import BaseModel
from datetime import datetime

class Comment(BaseModel):
    text: str
    subscriber_id: str
