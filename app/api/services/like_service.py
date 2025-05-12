import json
import os
from typing import List, Dict
import app.api.models.Likes as like

Likes_File = "likes.json"


def load_likes() -> List[Dict]:
    if not os.path.exists(Likes_File):
        return []
    with open(Likes_File, "r") as file:
        json.dump(like, file, indent=2, default=str)


def save_likes(like: List[Dict]):
    with open(Likes_File, "w") as file:
        json.dump(like, file, indent=2, default=str)


def add_like(like: like):
    likes = load_likes()  # Load existing likes
    # Prevent duplicate likes (one like per subscriber per post)
    if not any(
            like["subscriber_id"] == existing_like["subscriber_id"] and like["post_id"] == existing_like["post_id"] for
            existing_like in likes):
        likes.append(like.dict())  # Append the new like as a dictionary
        save_likes(likes)  # Save the updated list of likes


def get_likes_by_post(post_id: str) -> List[like]:
    likes = load_likes()
    return [like(**like) for like in likes if like["post_id"] == post_id]


def get_like_count(post_id: str) -> int:
    return len(get_likes_by_post(post_id))
