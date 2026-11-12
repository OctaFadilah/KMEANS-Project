# Earthquake K-Means Clustering & Spatial Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/ScikitLearn-%3E%3D1.1-orange?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-yellow)

An unsupervised machine learning project for spatial earthquake clustering using **K-Means**, optimized with the **Elbow Method** and **Silhouette Coefficient**. This repository contains clean data processing pipelines, evaluation scripts, and spatial visualization tools to group seismic events based on spatial coordinates (`latitude`, `longitude`), `depth`, and `magnitude`.

---

## 📂 Repository Structure

```text
KMEANS-Project/
│
├── Data/                      # Dataset files (earthquake CSV data)
├── images/                    # Visualizations and evaluation plots
│   ├── elbow_method.png       # Elbow Method curve (WCSS vs K)
│   └── silhouette_score.png   # Silhouette Score graph for K validation
│
├── Main.py                    # Main K-Means clustering pipeline
├── Plotting.py                # Spatial distribution and cluster visualization
├── elbowmethod.py             # Elbow Method script for optimal K
├── silhouettemethod.py        # Silhouette Score validation script
├── .gitignore                 # Files and directories ignored by Git
├── LICENSE                    # MIT License
├── requirements.txt           # Project dependencies and minimum versions
└── README.md                  # Project documentation
```

---

## 📊 Evaluation Methods

To ensure reliable clustering results, this project uses two complementary evaluation techniques across $K = 2$ to $10$ using standardized features:

1. **Elbow Method:** Evaluates model inertia (Within-Cluster-Sum-of-Squares) across a range of $K$ values to identify the optimal inflection point.
2. **Silhouette Coefficient:** Measures how similar an event is to its own cluster compared to other clusters, providing an objective score ranging from $-1$ to $1$.

---

## 🛠️ Prerequisites & Installation

1. Clone this repository:
   ```bash
   git clone [https://github.com/OctaFadilah/KMEANS-Project.git](https://github.com/OctaFadilah/KMEANS-Project.git)
   cd KMEANS-Project
   ```

2. Install the required dependencies using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Required Dependencies (`requirements.txt`)
- `scikit-learn>=1.1`
- `numpy>=1.23`
- `pandas>=1.5`
- `matplotlib>=3.6`
- `seaborn>=0.12`

---

## 🚀 Usage

Run the evaluation scripts first to determine the optimal number of clusters ($K$), then execute the main clustering and plotting pipelines:

```bash
# 1. Evaluate optimal K
python elbowmethod.py
python silhouettemethod.py

# 2. Run K-Means clustering and generate spatial plots
python Main.py
python Plotting.py
```

---

## 👥 Contributors

- [Daniel Kuncoro](https://github.com/DanielKuncoro)
- [Octa Fadilah](https://github.com/OctaFadilah)
