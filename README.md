# Earthquake K-Means Clustering

A machine learning project focused on grouping earthquake events based on spatial coordinates, depth, and magnitude using the K-Means clustering algorithm. This repository includes data preparation, evaluation metrics (Elbow Method & Silhouette Score), and visual plots to determine the optimal number of clusters ($K$).

---

## 📂 Repository Structure

```text
KMEANS-Project/
│
├── Data/                      # Dataset files (e.g., earthquake CSV data)
├── images/                    # Visualizations and evaluation plots
│   ├── elbow_method.png       # Elbow Method curve (WCSS vs K)
│   └── silhouette_score.png   # Silhouette Score graph for K validation
│
├── .gitignore                 # Files and directories ignored by Git
├── requirements.txt           # Project dependencies and minimum versions
└── README.md                  # Project documentation
```

---

## 📊 Evaluation Methods

To ensure reliable clustering results, this project uses two complementary evaluation techniques:

1. **Elbow Method:** Evaluates model inertia (Within-Cluster-Sum-of-Squares) across a range of $K$ values to find the optimal inflection point.
2. **Silhouette Coefficient:** Measures how similar an object is to its own cluster compared to other clusters, providing an objective score ranging from $-1$ to $1$.

---

## 🛠️ Prerequisites & Installation

To run this project locally, ensure you have Python installed, then install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Required Dependencies (`requirements.txt`)
* `scikit-learn>=1.1`
* `numpy>=1.23`
* `pandas>=1.5`
* `matplotlib>=3.6`
* `seaborn>=0.12`

---

## 👥 Contributors

- **Daniel Kuncoro**
- **Octa Fadilah**
