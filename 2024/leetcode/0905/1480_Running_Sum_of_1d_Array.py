from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        for i in range(len(nums)):
            new_num = nums[i] + (sums[i - 1] if i != 0 else 0)
            sums.append(new_num)
        return sums


class GptSolution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
