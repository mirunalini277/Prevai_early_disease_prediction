# z_score.py

import pandas as pd
import numpy as np

def compute_z_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes Z-score using historical residuals.
    """

    mean_residual = df["residual"].mean()
    std_residual = df["residual"].std()

    # Avoid division by zero
    if std_residual == 0 or np.isnan(std_residual):
        df["z_score"] = 0
    else:
        df["z_score"] = (df["residual"] - mean_residual) / std_residual

    return df
