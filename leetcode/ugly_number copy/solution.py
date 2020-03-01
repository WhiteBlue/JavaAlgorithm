PRIME_FACTORS = [2, 3, 5]


class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True
        for e in PRIME_FACTORS:
            if num % e == 0:
                val = int(num / e)
                if val == 1:
                    return True
                return self.isUgly(val)
        return False


