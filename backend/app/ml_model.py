import joblib
import pandas as pd
from pathlib import Path

# Get path to models directory
MODELS_DIR = Path(__file__).parent.parent.parent / "models"

# Load your saved files
print("Loading model files...")
rf_model = joblib.load(MODELS_DIR / "random_forest_model.pkl")
imputer = joblib.load(MODELS_DIR / "imputer.pkl")  # What's the filename?
feature_names = joblib.load(MODELS_DIR / "feature_names.pkl")  # What's the filename?
print(f"✓ Model loaded with {len(feature_names)} input features")


def predict_credit_risk(user_data: dict) -> dict:
    """
    Make credit risk prediction
    
    Args:
        user_data: Dict with 10 financial features
        
    Returns:
        Dict with credit_score, probability, risk_tier
    """
    # 1. Convert to DataFrame
    user_df = pd.DataFrame([user_data])[feature_names]  # Use feature_names
    
    # 2. Apply imputer (10 → 12 features)
    user_imputed = imputer.transform(user_df)  # Use imputer.transform()
    
    # 3. Get prediction
    prob = rf_model.predict_proba(user_imputed)[0][1]  # Use rf_model.predict_proba()
    
    # 4. Convert to credit score
    credit_score = int((1 - prob) * 100)
    
    # 5. Determine risk tier
    if credit_score >= 80:
        risk_tier = "Excellent"
    elif credit_score >= 70:
        risk_tier = "Good"
    elif credit_score >= 60:
        risk_tier = "fair"
    else:
        risk_tier = "poor"
    
    return {
        "credit_score": credit_score,
        "default_probability": float(prob),
        "risk_tier": risk_tier,
        "message": f"Your credit score is {credit_score} ({risk_tier})"
    }