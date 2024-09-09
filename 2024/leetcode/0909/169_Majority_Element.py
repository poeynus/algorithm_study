from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = {}
        for i in nums:
            num[i] = num.get(i, 0) + 1
        return max(num, key=num.get)


class OtherSolution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for i in nums:
            if count == 0:
                candidate = i

            count += 1 if candidate == i else count - 1
        return candidate

        # 이 문제에서는 완벽한 조건을 제시하므로, 다시 검증하지 않아도 됨
        # if nums.count(candidate) > len(nums) // 2:
        #     return candidate


OtherSolution().majorityElement([2, 2, 1, 1, 1, 2, 2])
