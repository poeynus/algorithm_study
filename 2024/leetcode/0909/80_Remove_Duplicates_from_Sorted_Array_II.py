from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        slow = 2  # 중복을 허용하는 부분의 끝을 추적하는 인덱스
        for fast in range(2, len(nums)):
            # 중복이 허용된 경우
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        print(nums)
        return slow


Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])

# 이 문제 부터 어렵네 이거
