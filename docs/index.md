# Chaewon Ha (하채원) — Research Portfolio

Policy researcher and Ph.D. candidate working at the intersection of
**administrative data, survival analysis, interpretable machine learning,
local-service infrastructure risk, and human-centered manufacturing systems.**

I translate field and biomechanical intuition into reproducible computational
models, and turn analysis into decision tools for policy and industry.

---

## Featured project
### Early Warning of Closure Risk in Neighborhood Sports Facilities

An early-warning model that estimates closure risk for neighborhood sports
facilities and identifies its drivers, so local governments can intervene
before service gaps appear.

**Pipeline:** synthetic data → Cox PH → tree ensembles (RF / XGBoost) →
SHAP attribution → SBRI composite ranking

→ Code & notebook: [local-infrastructure-closure-risk](https://github.com/anna90nana-lang/local-infrastructure-closure-risk)

> All figures below are produced on **synthetic data** that mirrors the
> structure of administrative records. No real or personal data is used.

#### 1. Survival curves (Kaplan–Meier)
How facility survival declines over time, by facility type.

![Kaplan-Meier](figures/km_curves.png)

#### 2. Interpretable hazard (Cox PH)
Direction and magnitude of each driver's effect on closure hazard.

![Cox hazard ratios](figures/cox_hr.png)

#### 3. Driver attribution (SHAP)
Which features drive predicted closure risk, and how.

![SHAP summary](figures/shap_summary.png)

#### 4. Operational risk index (SBRI)
A transparent composite score separating higher- and lower-risk facilities.

![SBRI distribution](figures/sbri_dist.png)

---

## Methods & tools
`Python` · `lifelines` (Cox PH) · `scikit-learn` · `XGBoost` · `SHAP` ·
`pandas` · `GeoPandas` · `SPSS / AMOS`

Survival analysis · interpretable ML · composite risk indices ·
spatial competition analysis · policy evaluation

---

## Other work (in progress)
- `sbri-dashboard-demo` — spatial risk index & early-warning dashboard (mock-up)
- `manufacturing-automation-readiness` — workforce / skill data for automation readiness (synthetic)

  ---

## Policy research experience

Researcher with **~60 policy research proposals** and multiple
government/municipal commissioned studies, spanning sports policy,
regional development, industry promotion, and accessibility.

### Selected commissioned projects
- **Small-business closure prediction model** — survival analysis &
  ML for early warning of business closure
- **Regional mid/long-term development plans** (e.g., Seongbuk-gu) —
  strategy frameworks, KPI design, evaluation
- **Game industry promotion strategy** (Daejeon) — sector analysis,
  policy roadmap
- **Game accessibility guidelines** (MCST & KOCCA, 2025) — contributed
  conceptual framework for accessibility
- **Organizational diagnosis** (anti-doping agency) — diagnostics,
  KPI/strategy system design
- **Education-development special zone** (Jeongeup) — needs analysis,
  policy design

### Academic record
- **5–6 peer-reviewed articles** in Korean academic journals (KCI)
- 1 conference presentation
- SCI manuscript in preparation (industrial biomechanics)

### Methods
Structural equation modeling (SPSS / AMOS) · survival analysis (Cox PH) ·
multi-criteria decision-making (AHP-GA) · multi-objective optimization
(NSGA-II) · input–output analysis · PSM-DID · spatial analysis (GIS / Kepler) ·
KPI & strategy-framework design

## Contact
GitHub: [@anna90nana-lang](https://github.com/anna90nana-lang)
