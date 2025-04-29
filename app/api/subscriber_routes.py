from fastapi import APIRouter
from app.api.models.subscriber import Subscriber
from app.api.services import subscriber_service

router = APIRouter()


@router.post("/", response_model=Subscriber)
def register_subscriber(name: str, email: str):
    subscriber = Subscriber.create(name, email)
    subscriber_service.add_subscriber(subscriber)
    return subscriber


@router.get("/")
def list_subscribers():
    return subscriber_service.load_subscribers()


@router.get("/{subscribers_id}")
def getById(subscribers_id: str):
    return subscriber_service.get_subscriber_by_id(subscribers_id)
