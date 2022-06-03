from fastapi import APIRouter, status, Depends, HTTPException, Response
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash

def create_user(db,request):
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.hashPassword(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db,id):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} does not exist.")
    return user