import pandas as pd
from anomaly_detection.risk_classifier import classify_risk

def test_risk_classifier():
    df = pd.DataFrame({
        "z_score": [0.5, 1.4, 2.6]
    })

    result = classify_risk(df)
    print("\n✅ Risk Classification Output:\n", result)

if __name__ == "__main__":
    test_risk_classifier()
