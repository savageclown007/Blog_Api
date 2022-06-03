from fastapi import APIRouter, status, Depends, HTTPException, Response
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog
from .. import oauth2



router = APIRouter()


@router.post('/blog', status_code=status.HTTP_201_CREATED,tags=['Blogs'])
def create(request: schemas.Blog, db:
           Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create_blog(request,db)

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['Blogs'])
def destroy(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)


@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['Blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(request,id,db)


@router.get('/blog', response_model=List[schemas.ShowBlog], status_code=status.HTTP_200_OK,tags=['Blogs'])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.get('/blog/{id}', response_model=schemas.ShowBlog, status_code=status.HTTP_200_OK,tags=['Blogs'])
def show(id, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get(id,db)
