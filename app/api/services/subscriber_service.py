from __future__ import annotations

import json
import os
from typing import List

from app.api.models.subscriber import Subscriber

SUBSCRIBER_FILE = "subscribers.json"


def load_subscribers() -> List[Subscriber]:
    if not os.path.exists(SUBSCRIBER_FILE):
        return []
    with open(SUBSCRIBER_FILE, "r") as f:
        data = json.load(f)
        return [Subscriber(**d) for d in data]


def save_subscribers(subscribers: List[Subscriber]):
    with open(SUBSCRIBER_FILE, "w") as f:
        json.dump([s.dict() for s in subscribers], f, indent=2)


def add_subscriber(subscriber: Subscriber):
    subscribers = load_subscribers()
    subscribers.append(subscriber)
    save_subscribers(subscribers)


def get_subscriber_by_id(subscriber_id: str) -> Subscriber | None:
    return next((s for s in load_subscribers() if s.id == subscriber_id), None)
