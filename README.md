# ALS Disease Severity

**Predicting amyotropic lateral sclerosis (ALS) disease severity from clinical and biomarker data.**

![Language](https://img.shields.io/badge/Python-3.9%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![pandas](https://img.shields.io/badge/pandas-data-150458)
![Domain](https://img.shields.io/badge/domain-biostatistics%20%2F%20clinical%20ML-success)

> **Status:** Early-stage research prototype. The repository contains the modelling
> and data-preparation scaffolding (feature handling, severity stratification,
> a gradient-boosting classifier, and cross-validation). It is intended to be run
> against the PRO-ACT ALS clinical-trials dataset, which is **not** redistributed here.

---

## Overview

Amyotropic lateral sclerosis (ALS) is a progressive neurodegenerative disease whose
clinical course varies widely between patients. Quantifying and predicting **disease
severity** is valuable for trial stratification, prognosis, and care planning.

This project frames severity assessment as a **supervised classification problem**:
given a patient's clinical features and biomarkers, predict a coarse severity band
(*mild / moderate / severe*) derived from the **ALSFRS-R** functional rating scale.

### Clinical motivation

- **ALSFRS-R** (Revised ALS Functional Rating Scale) scores patients from **0–48**
  (48 = full function) across 12 functional domains including speech, walking, and
  respiration. It is the standard functional endpoint in ALS clinical trials.
- Candidate biomarkers of interest in the research literature — and noted in this
  project's working notes — include **neurofilament light chain (NfL)** and
  **phosphorylated neurofilament heavy chain (pNfH)**.

---

## Data & Methodology

### Target definition

Continuous ALSFRS-R scores are discretised into three ordered severity bands
(`src/data_utils.py`):

| Band       | ALSFRS-R range |
|------------|----------------|
| `severe`   | 0–16           |
| `moderate` | 17–32          |
| `mild`     | 33–48          |

### Data preparation (`src/data_utils.py`)

- `load_als(path)` — loads the raw CSV and drops columns whose non-missing coverage
  falls below 60% (a `thresh`-based completeness filter) to reduce sparsity.
- `feature_summary(df)` — produces a per-column diagnostic of missingness percentage
  and cardinality to guide feature selection.
- `severity_groups(score)` — performs the ALSFRS-R → severity-band binning above.

### Model (`src/model.py`)

- **Estimator:** `GradientBoostingClassifier` (scikit-learn) with
  `n_estimators=200`, `learning_rate=0.05`, `max_depth=4`, `random_state=42`.
- **Evaluation:** `cv_score` runs **stratified k-fold cross-validation**
  (`StratifiedKFold`, shuffled, fixed seed) scored on **weighted F1**. Stratification
  is used deliberately because ALS severity bands are class-imbalanced.

The intended modelling target is the **PRO-ACT** corpus (Pooled Resource Open-Access
ALS Clinical Trials), a large pooled dataset of ALS clinical-trial records.

---

## Tech Stack & Tools

- **Python 3.9+**
- **scikit-learn** — `GradientBoostingClassifier`, `StratifiedKFold`, `cross_val_score`
- **pandas / NumPy** — data loading, missingness handling, binning

---

## Project Structure

```
ALS_Disease_Severity/
├── src/
│   ├── data_utils.py   # CSV loading, missingness filter, severity binning, feature summary
│   └── model.py        # Gradient-boosting classifier + stratified CV scoring
├── docs/
│   └── research.md     # Working research notes (ALSFRS-R, biomarkers, ML approach)
└── README.md
```

---

## Results

No fitted-model metrics, prediction outputs, or evaluation artifacts are committed to
this repository, and the PRO-ACT data is not included. To avoid misrepresentation, **no
performance figures are reported here.** Once the pipeline is run against PRO-ACT, the
`cv_score` helper returns mean and standard-deviation weighted-F1 across folds, which is
the metric to report.

---

## How to Reproduce

1. Obtain access to the PRO-ACT dataset and export a patient-level feature table to CSV,
   including an ALSFRS-R total-score column.
2. Install dependencies:
   ```bash
   pip install scikit-learn pandas numpy
   ```
3. Prepare data and labels, then train and evaluate:
   ```python
   from src.data_utils import load_als, severity_groups
   from src.model import train, cv_score

   df = load_als("proact_features.csv")
   y  = severity_groups(df["ALSFRS_R_Total"])
   X  = df.drop(columns=["ALSFRS_R_Total"])   # plus any further preprocessing

   model = train(X, y)
   print(cv_score(model, X, y))
   ```

---

## Challenges

- **Missing data:** clinical-trial records are sparse and irregular; the 60% coverage
  filter is a pragmatic first pass but discards potentially informative low-coverage
  features.
- **Class imbalance:** severity bands are unevenly populated, motivating stratified
  cross-validation and weighted F1 rather than raw accuracy.
- **Label discretisation:** binning a continuous functional score into three bands loses
  granularity and imposes fixed cut-points.

## Future Work

- Add explicit numeric/categorical preprocessing pipelines and imputation.
- Benchmark additional estimators and report calibrated, cross-validated metrics.
- Explore **ordinal** classification (severity bands are ordered) and survival/
  longitudinal modelling of ALSFRS-R trajectories.
- Incorporate NfL / pNfH biomarker features and quantify their predictive contribution.

## Conclusion

This repository provides a clean, honest starting point for ALS severity classification:
a reproducible data-prep and gradient-boosting pipeline with stratified evaluation,
ready to be applied to the PRO-ACT dataset. Reported results will be added once the model
is trained and evaluated on real data.

---

*Author: Fahil Ejaz*
