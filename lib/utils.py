from lib.array import Array
from lib.random import XorShiftRandom, LCGRandom

def generate_data(rng, rows, cols, low=0.0, high=10.0):
    return Array([
        [rng.uniform(low, high) for _ in range(cols)]
        for _ in range(rows)
    ])