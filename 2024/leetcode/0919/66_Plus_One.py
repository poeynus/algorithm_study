from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits.count(9) == len(digits):
            digits[:] = [1 if x == 0 else 0 for x in range(len(digits) + 1)]
            return digits
        elif digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits
            return digits


class OtherSolution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits


Solution().plusOne([8, 9, 9, 9])

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
#
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
#
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
