import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


class MergeSort:
    def __init__(self, x):
        self.arr = x

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(self, x=None):
        if x is None:
            x = self.arr
            
        if len(x) <= 1:
            return x
        
        mid = len(x) // 2
        left_half = self.sort(x[:mid])
        right_half = self.sort(x[mid:])
        
        return self.merge(left_half, right_half)
    
if __name__ == "__main__":
    A = [-5, 3, 2, 1, -3, -50, -3, 7, 2, 2]

    sorter = MergeSort(A)

    print(sorter.sort())
