MAP = {
    'I': 1,
    'V': 5,
    'IV': 4,
    'X': 10,
    'IX': 9,
    'XL': 40,
    'L': 50,
    'C': 100,
    'XC': 90,
    'D': 500,
    'CD': 400,
    'M': 1000,
    'CM': 900,
}


class Solution:
    def find_recursive(self, s, val):
        if not s:
            return val
        if len(s) > 1 and s[:2] in MAP:
            return self.find_recursive(s[2:], val + MAP[s[:2]])
        else:
            return self.find_recursive(s[1:], val + MAP[s[0]])

    def romanToInt(self, s: str) -> int:
        return self.find_recursive(s, 0)


if __name__ == '__main__':
    s = Solution()

    print(s.romanToInt("MCMXCIV"))
