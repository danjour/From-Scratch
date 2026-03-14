class Array:
    def __init__(self, data):
        self.data = self._parse(data)
        self.shape = self._compute_shape()

    def _parse(self, data):
        if len(data) == 0:
            return []
        if isinstance(data[0], (int, float)):
            return [list(data)]
        return [list(row) for row in data]

    def _compute_shape(self):
        rows = len(self.data)
        cols = len(self.data[0]) if rows > 0 else 0
        return (rows, cols)

    def __getitem__(self, idx):
        return self.data[idx]

    def __len__(self):
        return len(self.data)

    def __eq__(self, other):
        if isinstance(other, Array):
            return self.data == other.data
        return self.data == other

    def tolist(self):
        return self.data

    def copy(self):
        return Array([row[:] for row in self.data])

    def __repr__(self):
        return f"Array({self.data})"

    def min(self, axis=0):
        if len(self.data) == 0:
            raise ValueError("Array cannot be empty.")
        if axis != 0:
            raise NotImplementedError("Only axis=0 is supported.")
        try:
            result = self.data[0][:]
            for row in self.data[1:]:
                for d in range(len(row)):
                    if row[d] < result[d]:
                        result[d] = row[d]
            return result
        except TypeError as e:
            raise TypeError(f"Array must contain numeric values: {e}")
        except IndexError as e:
            raise IndexError(f"Array is malformed: {e}")

    def max(self, axis=0):
        if len(self.data) == 0:
            raise ValueError("Array cannot be empty.")
        if axis != 0:
            raise NotImplementedError("Only axis=0 is supported.")
        try:
            result = self.data[0][:]
            for row in self.data[1:]:
                for d in range(len(row)):
                    if row[d] > result[d]:
                        result[d] = row[d]
            return result
        except TypeError as e:
            raise TypeError(f"Array must contain numeric values: {e}")
        except IndexError as e:
            raise IndexError(f"Array is malformed: {e}")

    def mean(self, axis=0):
        if len(self.data) == 0:
            raise ValueError("Array cannot be empty.")
        n = len(self.data)
        cols = self.shape[1]
        return [
            sum(self.data[i][d] for i in range(n)) / n
            for d in range(cols)
        ]