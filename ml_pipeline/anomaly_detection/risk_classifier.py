# risk_classifier.py

import pandas as pd

def classify_risk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Assigns risk level based on Z-score.
    """

    def risk_logic(z):
        if z < 1:
            return "Normal"
        elif 1 <= z < 2:
            return "Medium"
        else:
            return "High"

    df["risk_level"] = df["z_score"].apply(risk_logic)

    return df
