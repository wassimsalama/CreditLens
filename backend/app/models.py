from pydantic import BaseModel, Field
from typing import Optional


class UserFinancialData(BaseModel):
    """User's financial information for credit assessment"""

    revolving_utilization: float = Field(
        ...,
        ge=0,
        le=1,
        description="Revolving credit utilization ratio",
        alias="RevolvingUtilizationOfUnsecuredLines"
    )

    age: int = Field(
        ...,
        ge=18,
        le=100,
        description="Age in years"
    )

    number_of_time_30_59_days_past_due: int = Field(
        ...,
        ge=0,
        alias="NumberOfTime30-59DaysPastDueNotWorse"
    )

    debt_ratio: float = Field(
        ...,
        ge=0,
        alias="DebtRatio"
    )

    monthly_income: Optional[float] = Field(
        None,
        ge=0,
        alias="MonthlyIncome"
    )

    number_of_open_credit_lines_and_loans: int = Field(
        ...,
        ge=0,
        alias="NumberOfOpenCreditLinesAndLoans"
    )

    number_of_times_90_days_late: int = Field(
        ...,
        ge=0,
        alias="NumberOfTimes90DaysLate"
    )

    number_real_estate_loans_or_lines: int = Field(
        ...,
        ge=0,
        alias="NumberRealEstateLoansOrLines"
    )

    number_of_time_60_89_days_past_due: int = Field(
        ...,
        ge=0,
        alias="NumberOfTime60-89DaysPastDueNotWorse"
    )

    number_of_dependents: Optional[int] = Field(
        None,
        ge=0,
        alias="NumberOfDependents"
    )

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "RevolvingUtilizationOfUnsecuredLines": 0.45,
                "age": 35,
                "NumberOfTime30-59DaysPastDueNotWorse": 1,
                "DebtRatio": 0.32,
                "MonthlyIncome": 5500,
                "NumberOfOpenCreditLinesAndLoans": 8,
                "NumberOfTimes90DaysLate": 0,
                "NumberRealEstateLoansOrLines": 1,
                "NumberOfTime60-89DaysPastDueNotWorse": 0,
                "NumberOfDependents": 2
            }
        }


class PredictionResponse(BaseModel):
    """Credit risk prediction result"""

    credit_score: int
    default_probability: float
    risk_tier: str
    message: str
