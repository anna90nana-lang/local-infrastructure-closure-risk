"""
Synthetic facility-survival data generator.
Mirrors the STRUCTURE of administrative licensing records — NOT real values.
No real administrative or personal data is used.
"""
import numpy as np
import pandas as pd
from pathlib import Path

def make_synthetic(n: int = 5000, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    # --- covariates ---
    X = pd.DataFrame({
        "tenure_yrs":      rng.exponential(6.0, n),
        "competitors_1km": rng.poisson(3.0, n),
        "floor_area":      rng.lognormal(5.0, 0.4, n),
        "facility_type":   rng.integers(0, 8, n),
    })

    # --- Cox-style linear predictor (higher => higher hazard) ---
    lp = (
        0.15 * X["competitors_1km"]      # more competition -> higher risk
        - 0.0008 * X["floor_area"]       # larger facility   -> lower risk
        - 0.05 * X["tenure_yrs"]         # longer tenure     -> lower risk
    )

    # baseline survival time ~ Exponential, scaled by exp(-lp)
    baseline = rng.exponential(5.0, n)
    T = baseline * np.exp(-lp)

    # administrative censoring at 5 years
    horizon = 5.0
    event = (T < horizon).astype(int)
    time = np.minimum(T, horizon)

    df = X.assign(time=np.round(time, 3), event=event)
    return df

if __name__ == "__main__":
    out = Path(__file__).resolve().parents[1] / "data"
    out.mkdir(exist_ok=True)
    df = make_synthetic()
    path = out / "synthetic_facilities.csv"
    df.to_csv(path, index=False)
    print(f"[ok] wrote {len(df)} rows -> {path}")
    print(df.head())
    print(f"event rate: {df['event'].mean():.3f}")
