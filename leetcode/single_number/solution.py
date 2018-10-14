class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = []
        for i in nums:
            if i in tmp:
                tmp.remove(i)
            else:
                tmp.append(i)

        return tmp.pop()

