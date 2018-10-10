class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        val = 0
        max_val = 0

        for i in range(0, len(prices)):
            if i + 1 == len(prices):
                break
            val += prices[i + 1] - prices[i]
            if val < 0:
                if val > max_val:
                    max_val = val
                val = 0
            else:
                if val > max_val:
                    max_val = val

        return max_val


