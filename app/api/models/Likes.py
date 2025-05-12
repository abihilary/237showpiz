from pydantic import BaseModel
from datetime import datetime


class Like(BaseModel):
    subscriber_id: str
    post_id: str
    timestamp: datetime = datetime.now()
