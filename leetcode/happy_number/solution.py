import math


class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 4:
            return False

        if n % 10 == 0:
            tmp = n
            while tmp >= 10:
                tmp = tmp / 10
            if tmp == 1:
                return True

        left_num = n
        num_list = []

        while left_num > 0:
            num_list.append(left_num % 10)
            left_num = int(left_num / 10)

        ret = 0
        for i in num_list:
            ret += math.pow(i, 2)

        return self.isHappy(ret)

