class XorShiftRandom:
    def __init__(self, seed):
        self.state = seed

    def _next_int(self):
        x = self.state
        x ^= (x << 13) & 0xFFFFFFFF  # XOR com shift left
        x ^= (x >> 17)               # XOR com shift right
        x ^= (x << 5) & 0xFFFFFFFF   # XOR com shift left
        self.state = x & 0xFFFFFFFF
        return self.state

    def random(self):
        return self._next_int() / 0xFFFFFFFF

    def uniform(self, low=0.0, high=1.0):
        return low + self.random() * (high - low)

    def randint(self, low, high):
        return low + self._next_int() % (high - low + 1)
    
    def choice(self, n, weights=None):
        if weights is None:
            weights = [1] * n
        total = sum(weights)
        cumulative_sum = 0
        cumulative = []
        for w in weights:
            cumulative_sum += w
            cumulative.append(cumulative_sum / total)

        r = self.random()

        for i, c in enumerate(cumulative):
            if r < c:
                return i
        return n - 1

class LCGRandom:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def _next_int(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def random(self):
        return self._next_int() / self.m

    def randint(self, low, high):
        return low + self._next_int() % (high - low + 1)

    def uniform(self, low=0.0, high=1.0):
        return low + self.random() * (high - low)

    def choice(self, n, weights=None):
        if weights is None:
            weights = [1] * n
        total = sum(weights)
        cumulative_sum = 0
        cumulative = []
        for w in weights:
            cumulative_sum += w
            cumulative.append(cumulative_sum / total)
        r = self.random()
        for i, c in enumerate(cumulative):
            if r < c:
                return i
        return n - 1