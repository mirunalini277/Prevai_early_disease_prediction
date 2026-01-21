import pandas as pd
from anomaly_detection.z_score import compute_z_score

def test_z_score():
    df = pd.DataFrame({
        "residual": [-2, 10]
    })

    result = compute_z_score(df)
    print("\n✅ Z-Score Output:\n", result)

if __name__ == "__main__":
    test_z_score()
