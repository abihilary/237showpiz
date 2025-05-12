from fastapi import APIRouter, HTTPException
from app.api.models.Likes import Like
import app.api.services.like_service as like_service

router = APIRouter()


@router.post("/", status_code=201)
def like_post(like: Like):
    like_service.add_like(like)
    return {"message": "Post liked successfully"}


@router.get("/", status_code=201)
def say_hi():

    return {"likes rout"}


@router.get("/post/{post_id}", response_model=int)
def get_post_like_count(post_id: str):
    return like_service.get_like_count(post_id)


@router.get("/post/{post_id}/details")
def get_post_likes(post_id: str):
    return [like.dict() for like in like_service.get_likes_by_post(post_id)]
