import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from lib.validators import Validator

# Time complexity: O(n^2)
# Space complexity: O(1)

class BubbleSort:
    def __init__(self, x):
        Validator.validate_numeric_list(x)
        self.arr = x

    def sort(self):
        for i in range (len(self.arr)):
             for j in range(0, len(self.arr) - i - 1):
                 if self.arr[j] > self.arr[j + 1]:
                     self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        return self.arr

if __name__ == "__main__":
    A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

    sorter = BubbleSort(A)

    print(sorter.sort())  # [-5, -3, -3, 1, 2, 2, 2, 3, 7]