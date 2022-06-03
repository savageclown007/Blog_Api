from fastapi import APIRouter, status, Depends, HTTPException, Response
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List


def create_blog(request,db: Session):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} does not exist")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(request,id,db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} does not exist")

    blog.update(
        dict(request))
    db.commit()
    return "updated"

def get_all(db):
    blogs = db.query(models.Blog).all()
    return blogs

def get(id,db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} does not exist.")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with id {id} does not exist."}
    return blog