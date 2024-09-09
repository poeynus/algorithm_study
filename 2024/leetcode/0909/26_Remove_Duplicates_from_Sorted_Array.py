from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1
        return len(nums)


class GPTSolution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        nums[:] = nums[: i + 1]
        return len(nums)


# nums = nums[:i+1] 과 nums[:] = nums[:i+1] 의 차이
# 전자는 새로운 리스트에 재할당을 하는 것이고 후자는 기존 리스트를 수정하는 것
# pop을 쓰는것만 생각했는데 성능이 많이 안좋다. 재할당을 생각하긴 했었는데, 리스트를 잘라서 넣으면 시간이 더 느릴거라 생각했는데 기존 리스트를 수정하며 저장하는 방법이 있는줄은 몰랐다.
