class Validator:

    @staticmethod
    def validate_numeric_list(data, name="Input"):
        if not isinstance(data, list):
            raise TypeError(f"{name} must be a list.")
        if len(data) == 0:
            raise ValueError(f"{name} cannot be empty.")
        if not all(isinstance(v, (int, float)) for v in data):
            raise TypeError(f"{name} must contain only numeric values.")
        if any(v != v for v in data):
            raise ValueError(f"{name} contains NaN values.")
        if any(abs(v) == float('inf') for v in data):
            raise ValueError(f"{name} contains infinite values.")