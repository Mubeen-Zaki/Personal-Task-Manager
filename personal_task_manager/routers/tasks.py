from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .. import models
from ..schemas import Task, ShowTask, UpdateTask, Logger, Status, CurrentUser
from ..database import get_db, get_mongodb
from typing import List
from ..services import tasks
from ..token import get_current_user 

router = APIRouter(tags=["Tasks"], prefix='/tasks')
collection = get_mongodb()

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_task(request_body: Task, db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return tasks.create_task(request_body, db, collection, current_user.id)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowTask])
async def get_tasks(db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return tasks.get_tasks(db, current_user.id)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowTask)
async def get_task(id: int, db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return tasks.get_task(id, db, current_user.id)

@router.delete('/{id}', status_code=status.HTTP_200_OK)
async def delete_task(id: int, db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return tasks.delete_task(id, db, collection, current_user.id)

@router.put('/update/{id}', status_code=status.HTTP_200_OK)
async def update_task(id: int, request_body: UpdateTask, db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return tasks.update_task(id, request_body, db, collection, current_user.id)

@router.put('/{id}', status_code=status.HTTP_200_OK)
async def update_status(id: int, completed: bool, db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return tasks.update_status(id, completed, db, collection, current_user.id)