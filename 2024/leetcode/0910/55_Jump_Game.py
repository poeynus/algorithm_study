from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0

        for i in range(len(nums)):
            if i > maxReach:
                return False

            maxReach = max(maxReach, i + nums[i])

            if maxReach >= len(nums) - 1:
                return True

        return False


Solution().canJump([3, 2, 1, 0, 4])

# 근시안적으로 가장 최적인 것을 해보자
# 2라면 1과 2 중 값이 더 큰것을 다음으로 선택하기 쭉 가자
# 실패하면 다른것 해보기
# greedy 알고리즘으로 풀건데, 요건이 무조건 최적해로 해결이 되어야만 가능한 문제네
