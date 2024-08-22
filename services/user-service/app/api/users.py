from fastapi import APIRouter, HTTPException
from app.models.users import User

router = APIRouter(prefix="/users", tags=["Users"])

# In-memory database substitute
users_db = []

@router.post("/", response_model=User, status_code=201)
def create_user(user: User):
    users_db.append(user)
    return user

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/", response_model=list[User])
def list_users():
    return users_db