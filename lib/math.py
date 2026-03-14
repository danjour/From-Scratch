class MathOps:
    @staticmethod
    def norm(v):
        if len(v) == 0:
            raise ValueError("Vector cannot be empty.")
        return sum(x ** 2 for x in v) ** 0.5

    @staticmethod
    def euclidean_distance(x, y):
        if len(x) != len(y):
            raise ValueError("Vectors must be of the same length.")
        diff = [x[d] - y[d] for d in range(len(x))]
        return MathOps.norm(diff)

    @staticmethod
    def manhattan_distance(x, y):
        if len(x) != len(y):
            raise ValueError("Vectors must be of the same length.")
        return sum(abs(x[d] - y[d]) for d in range(len(x)))
    
    @staticmethod
    def mean(values):
        if len(values) == 0:
            raise ValueError("Array cannot be empty.")
        return sum(values) / len(values)

    @staticmethod
    def variance(values, ddof=1):
        if len(values) == 0:
            raise ValueError("Array cannot be empty.")
        m = MathOps.mean(values)
        return sum((x - m) ** 2 for x in values) / (len(values) - ddof)

    @staticmethod
    def std(values, ddof=1):
        return MathOps.variance(values, ddof) ** 0.5

    @staticmethod
    def covariance(x, y, ddof=1):
        if len(x) != len(y):
            raise ValueError("Vectors must be of the same length.")
        mx = MathOps.mean(x)
        my = MathOps.mean(y)
        return sum((x[i] - mx) * (y[i] - my) for i in range(len(x))) / (len(x) - ddof)

        