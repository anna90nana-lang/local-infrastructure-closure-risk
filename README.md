# Early Warning of Closure Risk in Neighborhood Sports Facilities
Survival analysis + machine learning + spatial competition evidence (Korea).

> **Note on data.** This repository uses **synthetic sample data** that mirrors
> the *structure* (not the values) of administrative licensing records.
> No real administrative or personal data is included. The goal is to
> demonstrate a **reproducible analysis pipeline**, not to release data.

## Problem
Neighborhood sports facilities (gyms, swimming pools, etc.) close at high rates,
creating gaps in local service infrastructure. This project builds an
**early-warning model** that estimates closure risk and identifies its drivers,
so that local governments can intervene before service gaps appear.

## Data (synthetic)
A synthetic dataset of facility records with the following fields:

| field | type | description |
|---|---|---|
| `tenure_yrs` | float | years since business registration |
| `competitors_1km` | int | number of competing facilities within 1 km |
| `floor_area` | float | facility floor area (m²) |
| `facility_type` | int | facility category (0–7) |
| `time` | float | observed survival time (years, censored at 5) |
| `event` | int | 1 = closure observed, 0 = censored |

See `src/make_synthetic.py` for the generating process.

## Methods
1. **Cox proportional hazards** — baseline hazard & covariate effects (hazard ratios)
2. **Random Forest / XGBoost** — nonlinear closure prediction
3. **SHAP** — interpretable attribution of risk drivers
4. **SBRI (composite index)** — a transparent risk score for ranking/early warning

Each method answers a different question: Cox for *interpretable hazard*,
tree ensembles for *predictive accuracy*, SHAP for *driver attribution*,
SBRI for *operational ranking*.

## Results
Figures are generated into `figures/`:
- Kaplan–Meier survival curves by facility type
- Cox hazard-ratio forest plot
- SHAP summary (global driver importance)
- Risk-score distribution / ranking

## Policy / Business relevance
- Early-warning lists for local government intervention
- Prioritization of inspection / support resources
- Extensible to other local-service infrastructure (childcare, clinics, etc.)

## Reproduce
```bash
pip install -r requirements.txt
python src/make_synthetic.py        # creates data/synthetic_facilities.csv
jupyter notebook notebooks/01_analysis.ipynb
```

## Citation
If you refer to this work, please see `CITATION.cff`.

## License
MIT — see `LICENSE`.
