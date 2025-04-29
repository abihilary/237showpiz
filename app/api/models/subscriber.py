from pydantic import BaseModel, EmailStr
from uuid import uuid4

class Subscriber(BaseModel):
    id: str
    name: str
    email: EmailStr

    @staticmethod
    def create(name: str, email: str):
        return Subscriber(id=str(uuid4()), name=name, email=email)
