from typing import List


class MinStack:
    arr: List[int]
    min_index: int

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.min_index = -1

    def _find_min(self):
        min_index = 0
        for i in range(len(self.arr)):
            if self.arr[i] < self.arr[min_index]:
                min_index = i
        return min_index

    def push(self, x: int) -> None:
        self.arr.insert(0, x)
        self.min_index += 1

        if self.min_index >= 0:
            if self.arr[self.min_index] > x:
                self.min_index = 0
        else:
            self.min_index = 0

    def pop(self) -> None:
        self.arr.pop(0)
        if self.min_index == 0:
            self.min_index = -1
            if self.arr:
                self.min_index = self._find_min()
        else:
            self.min_index -= 1

    def top(self) -> int:
        return self.arr[0]

    def getMin(self) -> int:
        if self.min_index >= 0:
            return self.arr[self.min_index]
