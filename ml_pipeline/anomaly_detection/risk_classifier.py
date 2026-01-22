import pandas as pd

# -----------------------------
# Risk logic definition
# -----------------------------
def risk_logic(z_score):
    if z_score < 50:
        return "Low"
    elif z_score < 100:
        return "Medium"
    else:
        return "High"

# -----------------------------
# Existing dataframe-based API
# -----------------------------
def classify_risk(df):
    df = df.copy()
    df["risk_level"] = df["z_score"].apply(risk_logic)
    return df

# -----------------------------
# Single-value helper (NEW)
# -----------------------------
def classify_single_value(predicted_value):
    df = pd.DataFrame({"z_score": [predicted_value]})
    df["risk_level"] = df["z_score"].apply(risk_logic)
    return df["risk_level"].iloc[0]
