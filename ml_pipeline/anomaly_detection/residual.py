# residuals.py

import pandas as pd

def calculate_residuals(actual_df: pd.DataFrame,
                        predicted_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merges actual and predicted data and computes residuals.
    
    actual_df columns:
    date | district | disease | actual_cases
    
    predicted_df columns:
    date | district | disease | predicted_cases
    """

    merged = pd.merge(
        actual_df,
        predicted_df,
        on=["date", "district", "disease"],
        how="inner"
    )

    merged["residual"] = merged["actual_cases"] - merged["predicted_cases"]

    return merged
