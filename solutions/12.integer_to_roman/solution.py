MAP = {
    1: 'I',
    5: 'V',
    4: 'IV',
    10: 'X',
    9: 'IX',
    40: 'XL',
    50: 'L',
    100: 'C',
    90: 'XC',
    500: 'D',
    400: 'CD',
    1000: 'M',
    900: 'CM',
}

ARR = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


class Solution:
    def intToRoman(self, num: int) -> str:
        ret = []
        for v in ARR:
            if v <= num:
                times = int(num / v)
                for i in range(times):
                    ret.append(MAP[v])
                num -= times * v
        return ''.join(ret)


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(1994))
