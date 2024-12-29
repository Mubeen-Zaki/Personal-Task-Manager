from .. import models
from fastapi import HTTPException, status
from ..hashing import Hash
from bson import ObjectId

def get_user_history(db, collection, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found in the db!")
    data = collection.find({"user_id":user_id})
    data = data.to_list()
    if not data:
        data = {"message" : "No history found for the user!"}
    return data

def create_user(request_body, db):
    new_user = models.User(username=request_body.username, email=request_body.email, password=Hash.hash_password(request_body.password))
    try:
        db.add(new_user)
        db.commit()
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Problem with adding the user to the db!")
    return {"message":f"New user successfully added with user id : {new_user.id} !"}

def get_users(db):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found in the db!")
    return users

def get_user_details(db, user_id:int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found in the db!")
    return user  