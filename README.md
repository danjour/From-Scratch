# From Scratch

> Reimplementing fundamental algorithms and data structures without relying on external libraries. Each implementation is built using only core Python, focusing on understanding the underlying concepts.

---

## Philosophy

The goal of this repository is simple: **understand by building**.

Instead of calling `sklearn.cluster.KMeans` or `numpy.linalg.norm`, every component is written from the ground up — from random number generators to distance metrics. No shortcuts, no black boxes.

---

## Project Structure

```
from-scratch/
│
├── lib/
│   ├── array.py          # Custom n-dimensional array
│   ├── math_ops.py       # norm, euclidean, manhattan, mean, std, covariance
│   ├── random.py         # LCGRandom, XorShiftRandom
│   └── utils.py          # Shared utilities (e.g. generate_data)
│
├── ml/
│   ├── kmeans/
│   │   └── main.py       # K-Means Clustering
│   └── linear_regression/
│       └── main.py       # Linear Regression
│
├── data_structures/      # (coming soon)
├── sorting/              # (coming soon)
└── README.md
```

---

## Dependency Map

Each module only depends on lower-level modules — no circular dependencies.

```
array.py        →  nothing
math_ops.py     →  array.py
random.py       →  nothing
utils.py        →  array.py, random.py
ml/kmeans       →  array, math_ops, random, utils
ml/linear_reg   →  array, math_ops
```

---

## Implementations

### `lib/` — Shared Libraries

| Module | Contents |
|--------|----------|
| `array.py` | `Array` — storage, `min`, `max`, `mean` |
| `math_ops.py` | `MathOps` — `norm`, `euclidean_distance`, `manhattan_distance`, `mean`, `std`, `covariance` |
| `random.py` | `LCGRandom`, `XorShiftRandom` — `random`, `uniform`, `randint`, `choice` |
| `utils.py` | `generate_data` — combines `Array` + `Random` |

### `ml/` — Machine Learning

| Algorithm | Description | Status |
|-----------|-------------|--------|
| K-Means Clustering | Unsupervised clustering with configurable metric and seed | ✅ Done |
| Linear Regression | Simple linear regression with correlation and slope | ✅ Done |
| Decision Tree | — | 🔜 Soon |
| Neural Network (MLP) | — | 🔜 Soon |

### `data_structures/` — Data Structures

| Structure | Status |
|-----------|--------|
| Linked List | 🔜 Soon |
| Binary Tree | 🔜 Soon |

### `sorting/` — Sorting Algorithms

| Algorithm | Status |
|-----------|--------|
| Bubble Sort | 🔜 Soon |
| Quick Sort | 🔜 Soon |

---

## Example — K-Means from Scratch

```python
from lib.random import XorShiftRandom
from lib.utils import generate_data
from ml.kmeans.main import KMeansClustering

# Generate random data
rng = XorShiftRandom(seed=42)
data = generate_data(rng, rows=100, cols=2, low=0.0, high=10.0)

# Fit the model
kmeans = KMeansClustering(n_clusters=3, metric='euclidean')
kmeans.fit(data)

print("Cluster Centers:", kmeans.centers)
print("Labels:", kmeans.labels)
```

## Example — Linear Regression from Scratch

```python
from lib.array import Array
from ml.linear_regression.main import LinearRegression

x = Array([1.0, 2.0, 3.0, 4.0, 5.0])
y = Array([2.1, 4.0, 5.9, 8.2, 9.8])

model = LinearRegression(x, y)
print("Prediction for x=6:", model.predict(6.0))
```

---

## Design Principles

- **No external libraries** — only Python's standard library
- **Separation of concerns** — each module has a single responsibility
- **No circular dependencies** — `lib/` flows in one direction
- **Explicit over implicit** — no magic, no shortcuts
- **Readable over clever** — code should teach, not impress

---

## Dependencies

```
python >= 3.8
matplotlib  # only for visualization
```

> All core algorithms run with zero dependencies.

---

## License

MIT