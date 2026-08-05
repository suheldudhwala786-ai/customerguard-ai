import shap
import pandas as pd
import numpy as np
import xgboost as xgb
from typing import Dict, Any

class SHAPEngine:
    """Enterprise SHAP explainability engine for churn predictions."""
    def __init__(self, model: xgb.XGBClassifier, X_train: pd.DataFrame):
        self.model = model
        self.explainer = shap.TreeExplainer(model)
        self.X_train = X_train

    def get_local_explanation(self, instance: pd.DataFrame) -> Dict[str, Any]:
        """Generates SHAP values for a single prediction."""
        shap_values = self.explainer.shap_values(instance)
        feature_names = self.X_train.columns.tolist()
        
        # Convert shap values to dictionary
        contributions = dict(zip(feature_names, shap_values[0] if isinstance(shap_values, list) else shap_values[0]))
        
        # Get top drivers
        sorted_contributions = sorted(contributions.items(), key=lambda x: abs(x[1]), reverse=True)
        
        return {
            "base_value": float(self.explainer.expected_value),
            "contributions": contributions,
            "top_drivers": sorted_contributions[:5]
        }
