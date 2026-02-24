from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from .service import create_user,authenticate_user,generate_token
from app.database import get_db
from app.schemas.user import UserRegister, Token, UserLogin

router = APIRouter(tags=["authentication"],prefix="/auth")

@router.post("/register")
async def register(user:UserRegister,db:Session=Depends(get_db)):
    existing_user = db.query(user.email==User.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Email already registerd")
    create_user(db,user.email,user.password)
    return {"message":"user registerd successfully"}

@router.post("/login",response_model=Token)
async def login(user:UserLogin,db:Session=Depends(get_db)):
    db_user = authenticate_user(db,user.email,user.password)
    if  not db_user:
        raise HTTPException(status_code=401,detail="invalid credentials")

    access_token = generate_token(db_user)
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }
