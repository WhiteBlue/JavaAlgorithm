from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums = sorted(nums)
        tmp = set()

        for i in range(0, len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    arr = [nums[i], nums[j], nums[k]]
                    if str(arr) not in tmp:
                        tmp.add(str(arr))
                        ret.append(arr)
                    j += 1
                    k -= 1

        return ret

