from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database import SessionLocal
from app.models import User
from app.auth import verify_password, create_access_token, hash_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

# ✅ TEMP: Reset admin password
@router.get("/reset-admin")
def reset_admin(db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == "admin@assetvault.com").first()
    if user:
        user.hashed_password = hash_password("admin123")
        db.commit()
        return {"message": "✅ Password reset successfully!"}
    return {"message": "❌ User not found"}