class Solution(object):

    def __init__(self):
        self.buf = []
        self.ret = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.find_in(candidates, target, 0, 0)
        return self.ret

    def find_in(self, candidates, target, index, val):
        if val == target:
            copy = []
            for i in self.buf:
                copy.append(i)
            copy = sorted(copy)
            if copy not in self.ret:
                self.ret.append(copy)
        elif val < target:
            for i in range(index, len(candidates)):
                self.buf.append(candidates[i])
                self.find_in(candidates, target, i, val + candidates[i])
                self.buf.pop()
