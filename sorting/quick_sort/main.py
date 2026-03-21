import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


class QuickSort:
    def __init__(self, x):
        self.arr = x

    def partition(self, x, low, high):
        pivot = x[high]
        i = low - 1
        for j in range(low, high):
            if x[j] <= pivot:
                i += 1
                x[i], x[j] = x[j], x[i]
        x[i + 1], x[high] = x[high], x[i + 1]
        return i + 1

    def sort(self, x=None, low=0, high=None):
        if x is None:
            x = self.arr
            
        if high is None:
            high = len(x) - 1
            
        if low < high:
            pi = self.partition(x, low, high)
            
            self.sort(x, low, pi - 1)
            
            self.sort(x, pi + 1, high)
            
        return x
    
if __name__ == "__main__":
    A = [-5, 3, 2, 1, -3, -50, -3, 7, 2, 2]

    sorter = QuickSort(A)

    print(sorter.sort())
