import json
import os
from typing import List, Dict
from app.api.models.Comment import Comment  # Make sure it's lowercase if your filename is lowercase

COMMENTS_FILE = "comments.json"
SUBSCRIBERS_FILE = "subscribers.json"


def load_subscribers() -> List[Dict]:
    if not os.path.exists(SUBSCRIBERS_FILE):
        return []
    with open(SUBSCRIBERS_FILE, "r") as f:
        return json.load(f)


def get_subscriber_name(subscriber_id: str) -> str:
    subscribers = load_subscribers()
    for subscriber in subscribers:
        if subscriber['id'] == subscriber_id:
            return subscriber.get('name', 'Unknown')
    return 'Unknown'


def load_comments_file() -> Dict[str, List[dict]]:
    if not os.path.exists(COMMENTS_FILE):
        return {}
    with open(COMMENTS_FILE, "r") as file:
        return json.load(file)


def save_comments_file(data: Dict[str, List[dict]]):
    with open(COMMENTS_FILE, "w") as file:
        json.dump(data, file, indent=2, default=str)


def load_all_comments() -> List[Comment]:
    data = load_comments_file()
    all_comments = []
    for comments in data.values():
        all_comments.extend(Comment(**item) for item in comments)
    return all_comments


def get_comments_by_subscriber(subscriber_id: str) -> List[Comment]:
    data = load_comments_file()
    return [Comment(**item) for item in data.get(subscriber_id, [])]


def add_comment(comment: Comment):
    data = load_comments_file()
    subscriber_comments = data.get(comment.subscriber_id, [])
    # Increment comment count
    comment.comment_count = len(subscriber_comments) + 1
    subscriber_comments.append(comment.dict())
    data[comment.subscriber_id] = subscriber_comments
    save_comments_file(data)


def add_comments_batch(comments: List[Comment]):
    data = load_comments_file()
    for comment in comments:
        subscriber_comments = data.get(comment.subscriber_id, [])
        comment.comment_count = len(subscriber_comments) + 1
        subscriber_comments.append(comment.dict())
        data[comment.subscriber_id] = subscriber_comments
    save_comments_file(data)


def get_comments_by_post_id(post_id: str) -> List[Comment]:
    all_comments = load_all_comments()
    return [comment for comment in all_comments if comment.post_id == post_id]
