from sqlalchemy.orm import Session
from app.repositories.base_repository import BaseRepository
from app.models.user import User
from app.core.security import get_password_hash
from typing import Optional

class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = BaseRepository(User)

    def create_user(self, email: str, password: str, org_id: str, role: str = "member") -> User:
        hashed_password = get_password_hash(password)
        user_data = {
            "email": email,
            "password_hash": hashed_password,
            "org_id": org_id,
            "role": role
        }
        return self.repository.create(self.db, user_data)

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email, User.is_active == True).first()
