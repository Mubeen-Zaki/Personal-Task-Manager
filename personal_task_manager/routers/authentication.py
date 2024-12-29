from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..hashing import Hash
from ..token import create_access_token
from ..schemas import Token

router = APIRouter(tags=['Authentication'])

@router.post('/login')
async def login(request_body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request_body.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials!")
    if not Hash.verify_password(request_body.password, user.password):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Password is incorrect!")
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return Token(access_token=access_token, token_type="bearer")
