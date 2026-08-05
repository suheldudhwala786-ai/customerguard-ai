from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.ml.inference.predictor import EnterprisePredictor
from app.api.deps import get_current_user
from app.models.user import User
from typing import List, Dict, Any

router = APIRouter()
predictor = EnterprisePredictor()

@router.post("/", summary="Generate churn prediction")
async def predict_churn(
    data: Dict[str, Any],
    current_user: User = Depends(get_current_user)
):
    """
    Predict churn probability for a single customer.
    Includes SHAP-based explainability and risk assessment.
    """
    return predictor.predict(data)

@router.post("/batch", summary="Batch churn prediction")
async def batch_predict_churn(
    data_list: List[Dict[str, Any]],
    current_user: User = Depends(get_current_user)
):
    """Predict churn for a batch of customers."""
    return predictor.batch_predict(data_list)
