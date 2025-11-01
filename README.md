Here’s a polished **`README.md`** version of your project description — formatted, structured, and styled for clarity and professionalism on GitHub:

---

# 🧠 ALS Progression Subtyping and Predictive Modeling

This repository contains the analysis notebook for a project focused on understanding the **heterogeneity of Amyotrophic Lateral Sclerosis (ALS) progression** and developing **predictive models for disease severity** using longitudinal clinical data.

The analysis identifies **distinct patient subgroups (phenotypes)** based on multivariate temporal features and models disease severity within these identified clusters.

---

## 📂 Project Structure

| File                               | Description                                                                                                                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`als-clinic-unina24july.ipynb`** | Main Jupyter Notebook containing the full pipeline: from EDA and preprocessing to subtyping (clustering) and predictive modeling (GLM/Bayesian models). |
| **`DF_SLA_ST.csv`**                | Expected dataset containing longitudinal clinical measurements — functional scores, motor strength, and disease progression markers.                    |

---

## 🎯 Methodology Overview

The analysis follows a **sequential statistical learning pipeline**:

### 1. Data Preparation and Exploratory Analysis (EDA)

* **Data Source:** Clinical data from the *ALS Clinic, University of Naples Federico II*.
* **Cleaning:** Handling missing values (particularly in Spirometry data) and converting date fields.
* **Filtering:** Patients with fewer than three visits were excluded to ensure robust longitudinal analysis.
* **Visualization:** Distribution analysis of prognostic variables such as:

  * `Age_at_onset`
  * `Diagnostic_delay`
  * `Progression_rate`
  * `ALSFRS_R`
  * `ALSAQ_5`

---

### 2. Patient Subtyping (Triclustering & Clustering)

Objective: Identify **patient subgroups with similar progression patterns** across multiple features over time.

* **Triclustering:** Custom triclustering algorithm applied to a scaled 3D tensor (patients × visits × features) to detect cohesive blocks.
* **Dimensionality Reduction:** UMAP (Uniform Manifold Approximation and Projection) used to visualize tricluster memberships.
* **Clustering:** Hierarchical (Agglomerative) Clustering on UMAP embeddings revealed **three progression profiles** (e.g., “Slow Progressor,” “Fast Progressor,” etc.).

---

### 3. Predictive Modeling (Generalized Linear Models)

Validated the **clinical relevance** of the discovered patient clusters by modeling **ordinal disease severity (KINGS_Total score)**.

* **Feature Selection:**
  Recursive Feature Elimination (RFE) and Mutual Information (MI) identified key predictors:

  * `Progression_rate`
  * `Disease_duration`
  * `Age_at_onset`
  * `MRC_Upper_Limb`
  * `MRC_Bulbar`
  * `PUMNS_Upper_Limb`
* **Frequentist Models:** Ordinal and Multinomial Logistic Regression models were fitted for each patient cluster.
* **Bayesian Mixed-Effects Models:** Hierarchical Ordinal and Nominal Logit models (PyMC/Bambi) included `Tricluster_Label` as a random intercept to capture between-cluster variability.

---

## ✨ Key Findings

* **Cluster Heterogeneity:**
  Clustering effectively segregated patients into progression profiles (e.g., *Slow vs. Fast Progressors*), confirming strong heterogeneity in disease trajectories.

* **Primary Drivers of Severity:**
  In Bayesian models, **Progression Rate** and **Disease Duration** consistently emerged as the strongest predictors of higher `KINGS_Total` scores.

* **Model Performance:**
  The **Bayesian Nominal Mixed-Effects Model (Bambi)** achieved the best performance with **WAIC deviance ≈ 2870.29**, offering nuanced, category-specific effects for predictors.

---

## 🛠 Requirements

Install dependencies directly within the notebook using:

```bash
!pip install bambi pymc arviz numpy pandas scikit-learn umap-learn seaborn statsmodels
```

### Core Libraries

* `bambi`
* `pymc`
* `arviz`
* `numpy`
* `pandas`
* `scikit-learn`
* `umap-learn`
* `seaborn`
* `statsmodels`

---

## 👥 Authors

* **Fahil Ejaz (India)**
* **Oguz Erden (Turkey)**
* **Fauzan Ejaz (India)**

**Acknowledgments:**
Special thanks to 
*Professor Giulia Vannucci* and 
*Professor Roberta Siciliano*,
**University of Napoli Federico II (Advanced Statistics).**

---

## 🧩 Citation

If you use or reference this analysis, please cite as:

> Ejaz, F., 
Erden, O., 
Ejaz, F. (2025). 
*ALS Progression Subtyping and Predictive Modeling*. University of Napoli Federico II.

