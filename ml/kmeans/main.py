from lib.array import Array
from lib.random import XorShiftRandom
from lib.math_ops import MathOps
from lib.utils import generate_data
  
class KMeansClustering:
    def __init__(self, n_clusters=3, max_iters=100, init='random', seed=42):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.init = init
        self.rng = XorShiftRandom(seed)

    def _init_centers(self, X):
        mins = X.min(axis=0)
        maxs = X.max(axis=0)
        return Array([
            [self.rng.uniform(mins[d], maxs[d]) for d in range(X.shape[1])]
            for _ in range(self.n_clusters)
        ])

    def _compute_distances(self, X, centers):
        distances = []
        for point in X:
            row = []
            for center in centers:
                row.append(MathOps.euclidean_distance(point, center))
            distances.append(row)
        return distances

    def fit(self, X):
        self.centers = self._init_centers(X)

        for _ in range(self.max_iters):
            distances = self._compute_distances(X, self.centers)
            self.labels = [row.index(min(row)) for row in distances]

            new_centers = []
            for i in range(self.n_clusters):
                cluster_points = [X[j] for j in range(len(X)) if self.labels[j] == i]
                if len(cluster_points) == 0:
                    new_centers.append(self.centers[i])
                    continue
                center = [
                    sum(p[d] for p in cluster_points) / len(cluster_points)
                    for d in range(X.shape[1])
                ]
                new_centers.append(center)

            if new_centers == self.centers.tolist():
                break
            self.centers = Array(new_centers)

    def predict(self, X):
        distances = self._compute_distances(X, self.centers)
        return [row.index(min(row)) for row in distances]
    
if __name__ == "__main__":
    rng = XorShiftRandom(seed=42)

    data = generate_data(rng, rows=100, cols=2, low=0.0, high=10.0)

    kmeans = KMeansClustering(n_clusters=3)

    kmeans.fit(data)
    
    print("Cluster Centers:", kmeans.centers)

    print("Labels:", kmeans.labels)

    # Points of clusters
    points = data.tolist()
    xs, ys = zip(*points)

    # Centroids
    centers = kmeans.centers.tolist()
    cxs, cys = zip(*centers)
