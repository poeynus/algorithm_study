from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        for i, num in enumerate(nums):
            if target < num:
                return i

        return len(nums)


class OtherSolution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#
# nums = [3,6,7,8,10]
# target = 5
