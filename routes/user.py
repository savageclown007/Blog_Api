from fastapi import APIRouter, status, Depends, HTTPException, Response
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter()

@router.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser,tags=['Users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(db,request)
   


@router.get('/user/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK,tags=['Users'])
def getUser(id: int, db: Session = Depends(get_db)):
    return user.get_user(db,id)
