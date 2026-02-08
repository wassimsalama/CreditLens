from fastapi import FastAPI

from app.models import UserFinancialData, PredictionResponse
from app.ml_model import predict_credit_risk

app = FastAPI(
    title="CFEditLens API",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict(data: UserFinancialData):
    user_dict = data.model_dump(by_alias=True)
    return predict_credit_risk(user_dict)
