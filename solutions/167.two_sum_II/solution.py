from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if numbers[i] <= target:
                if target - numbers[i] in numbers:
                    return [i + 1, numbers.index(target - numbers[i], i + 1) + 1]
        return []


if __name__ == '__main__':
    s = Solution()

    print(s.twoSum([2, 7, 11, 15], 9))
