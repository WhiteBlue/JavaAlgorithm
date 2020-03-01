from _ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        add_val = 0
        tmp = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                add_val += diff
        return add_val
