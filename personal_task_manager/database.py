from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pymongo.mongo_client import MongoClient
from fastapi import status, HTTPException
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv("personal_task_manager\\.env")

# Access the variables
DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

database_name = ".tasks.db"
database_url = f"sqlite:///{database_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(database_url, connect_args=connect_args)

session_factory = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    try:
        session = session_factory()
        yield session
    finally:
        session.close()

def get_mongodb():
    try:
        print("*" * 100)
        print(DB_CONNECTION_STRING)
        client = MongoClient(DB_CONNECTION_STRING)
        db = client["Personal_Task_Manager"]
        collection = db["tasks"]
    except Exception as e:
        print(str(e))
    else:
        return collection