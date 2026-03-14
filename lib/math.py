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