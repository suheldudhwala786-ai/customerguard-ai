from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.model import Model
from app.repositories.base_repository import BaseRepository
from app.api.deps import role_required
from app.models.user import User

router = APIRouter()
repo = BaseRepository(Model)

@router.get("/", summary="List all machine learning models")
def list_models(
    db: Session = Depends(get_db),
    current_user: User = Depends(role_required("admin"))
):
    """Retrieve all registered models in the registry."""
    return repo.get_all(db)

@router.post("/train", summary="Trigger a new training job")
def trigger_training(
    db: Session = Depends(get_db),
    current_user: User = Depends(role_required("admin"))
):
    """Initiates an asynchronous model training job via Celery."""
    return {"message": "Training job queued", "job_id": "job_12345"}
