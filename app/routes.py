from fastapi import APIRouter
from dependency import db_dependency
from schema import User
import model
router = APIRouter()

@router.post("/create-user")
def create_user(user:User, db:db_dependency):
    try:
        db_user = model.Users(username=user.name, email=user.email, password=user.password,is_active=user.is_active)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        db.rollback()
        return {"error":str(e)}
    return {"user":user}
