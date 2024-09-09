from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            rotate_count = k % len(nums)
            for i in range(rotate_count):
                nums.insert(0, nums.pop())
        else:
            nums[:] = nums[len(nums) - k :] + nums[: len(nums) - k]


class GPTSolution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # k가 n보다 클 경우를 대비해 회전 수를 줄임
        self.reverse(nums, 0, n - 1)
        # Step 2: 처음 k개의 요소를 뒤집기
        self.reverse(nums, 0, k - 1)
        # Step 3: 나머지 요소들을 뒤집기
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        """리스트의 일부를 뒤집는 함수"""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


Solution().rotate([1, 2, 3, 4, 5, 6, 7], 7)
# 오 이번엔 좀 잘 생각한듯
