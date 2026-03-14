import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from lib.validators import Validator

# Time complexity: O(n^2)
# Space complexity: O(1)

class SelectionSort:
    def __init__(self,x):
        Validator.validate_numeric_list(x)
        self.arr = x

    def sort(self):
        for i in range(1, len(self.arr)):
            min_idx = 1
            for j in range(i+1,len(self.arr)):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx =  j
            self.arr[i], self.arr[min_idx] = self.arr[min_idx],self.arr[i]

        return self.arr

if __name__ == "__main__":
    A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

    sorter = SelectionSort(A)

    print(sorter.sort())  # [-5, -3, -3, 1, 2, 2, 2, 3, 7]