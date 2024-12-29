from fastapi import APIRouter, status, Depends, HTTPException
from .. import models
from ..database import get_mongodb, get_db
from sqlalchemy.orm import Session
from ..schemas import CurrentUser, ShowUser, ShowUserDetails, User, Logger
from typing import List
from ..hashing import Hash
from ..services import users
from ..token import get_current_user
from bson import ObjectId

router = APIRouter(tags=['User'], prefix="/users")
collection = get_mongodb()

@router.get('/history', status_code=status.HTTP_200_OK, response_model=List[Logger])
async def get_user_history(db:Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return users.get_user_history(db, collection, current_user.id)
    
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(request_body: User, db: Session = Depends(get_db)):
    return users.create_user(request_body, db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowUser])
async def get_users(db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return users.get_users(db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=ShowUserDetails)
async def get_user_details(db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return users.get_user_details(db, current_user.id)