class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = [int(part) for part in version1.split('.')]
        arr2 = [int(part) for part in version2.split('.')]

        max_len = max(len(arr1), len(arr2))
        num1, num2, offset = 0, 0, 10 ** max_len

        for i in range(max_len):
            if i < len(arr1):
                num1 += int(arr1[i] * offset)
            if i < len(arr2):
                num2 += int(arr2[i] * offset)
            offset /= 10

        if num1 == num2:
            return 0
        return int((num1 - num2) / abs(num1 - num2))

