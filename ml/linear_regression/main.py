import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from lib.math import MathOps

class LinearRegression:
    def __init__(self, x, y):
        self._validate(x, y)
        self.x = x
        self.y = y
        self._std_x = MathOps.std(x)
        self._std_y = MathOps.std(y)
        self._mean_x = MathOps.mean(x)
        self._mean_y = MathOps.mean(y)
        self.cov = MathOps.covariance(self.x, self.y)
        self._correlation = self._compute_correlation()
        self._slope = self._compute_slope()
        self._intercept = self._compute_intercept()

    def _validate(self, x, y):
        if len(x) == 0 or len(y) == 0:
            raise ValueError("Input arrays cannot be empty.")
        if len(x) != len(y):
            raise ValueError("x and y must have the same length.")
        if len(x) < 2:
            raise ValueError("At least 2 data points are required.")
        if not all(isinstance(v, (int, float)) for v in x):
            raise TypeError("x must contain only numeric values.")
        if not all(isinstance(v, (int, float)) for v in y):
            raise TypeError("y must contain only numeric values.")
        if any(v != v for v in x):
            raise ValueError("x contains NaN values.")
        if any(v != v for v in y):
            raise ValueError("y contains NaN values.")
        if any(abs(v) == float('inf') for v in x):
            raise ValueError("x contains infinite values.")
        if any(abs(v) == float('inf') for v in y):
            raise ValueError("y contains infinite values.")
        if len(set(x)) == 1:
            raise ValueError("All x values are the same. Cannot compute slope.")

    def _compute_correlation(self):
        
        return self.cov / (self._std_x * self._std_y)

    def _compute_slope(self):
        return self._correlation * (self._std_y / self._std_x)

    def _compute_intercept(self):
        return self._mean_y - self._slope * self._mean_x

    def predict(self, value):
        return self._intercept + self._slope * value
    

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    model = LinearRegression(x, y)

    print("Slope:", model._slope)
    print("Intercept:", model._intercept)
    print("Correlation:", model._correlation)

    test_value = 6
    prediction = model.predict(test_value)
    print(f"Prediction for x={test_value}: {prediction}")