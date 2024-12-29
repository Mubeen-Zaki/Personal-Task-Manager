from .. import models
from fastapi import HTTPException, status
from datetime import datetime
from ..schemas import Logger, Status

def create_task(request_body, db, collection, user_id: int):
    new_task = models.Tasks(title=request_body.title, description=request_body.description, deadline=request_body.deadline, completed=request_body.completed, user_id=user_id)
    try:
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Problem with adding the task to the db!")
    log = Logger(user_id=user_id, task_id= new_task.id, title=new_task.title, timestamp=datetime.now(), description=f"User with id : {user_id} added task titled {new_task.title} at {str(datetime.now())} whose task id is {new_task.id}")
    collection.insert_one(log.model_dump())
    return {"message":"New task successfully added!"}

def get_tasks(db, user_id:int):
    tasks = db.query(models.Tasks).filter(models.Tasks.user_id == user_id).all()
    if not tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Problem with finding the tasks for the user")
    return tasks

def get_task(id, db, user_id:int):
    tasks = db.query(models.Tasks).filter(models.Tasks.id == id and models.Tasks.user_id == user_id).first()
    if not tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Problem with finding the tasks for the user")
    return tasks

def delete_task(id, db, collection, user_id:int):
    task = db.query(models.Tasks).filter(models.Tasks.id == id and models.Tasks.user_id == user_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id : {id} doesn't exist for the user in the db!")
    db.delete(task)
    db.commit()
    log = Logger(user_id=user_id, task_id= task.id, title=task.title, timestamp=datetime.now(), description=f"User with id : {user_id} deleted task titled {task.title} at {str(datetime.now())} whose task id is {task.id}")
    collection.insert_one(log.model_dump())
    return {"message":"New task successfully added!"}

def update_task(id, request_body, db, collection, user_id:int):
    task = db.query(models.Tasks).filter(models.Tasks.id == id and models.Tasks.user_id == user_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id : {id} doesn't exist for the user in the db!")
    update_data = request_body.model_dump()
    update_data = {key:value for key, value in update_data.items() if value is not None}
    if update_data:
        db.query(models.Tasks).filter(models.Tasks.id == id and models.Tasks.user_id == user_id).update(update_data, synchronize_session=False)
    db.commit()
    log = Logger(user_id=user_id, task_id= task.id, title=task.title, timestamp=datetime.now(), description=f"User with id : {user_id} updated the task details of task titled {task.title} at {str(datetime.now())} whose task id is {task.id} with the data : {update_data}")
    collection.insert_one(log.model_dump())
    return {"message":"New task successfully added!"}

def update_status(id, completed, db, collection, user_id:int):
    task = db.query(models.Tasks).filter(models.Tasks.id == id and models.Tasks.user_id == user_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id : {id} doesn't exist for the user in the db!")
    db.query(models.Tasks).filter(models.Tasks.id == id and models.Tasks.user_id == user_id).update({models.Tasks.completed : completed}, synchronize_session=False)
    db.commit()
    log = Logger(user_id=user_id, task_id= task.id, title=task.title, timestamp=datetime.now(), description=f"User with id : {user_id} updated the status of the task titled {task.title} as {Status.done if completed else Status.not_done} at {str(datetime.now())} whose task id is {task.id}")
    collection.insert_one(log.model_dump())
    return {"message":"Status updated successfully!"}  