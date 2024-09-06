class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
                cnt += 1
            else:
                num -= 1
                cnt += 1
        return cnt


class OtherSolution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num > 0:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            cnt += 1
        return cnt


class GPTSolution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num > 0:
            if num & 1:  # 홀수인 경우
                num -= 1
            else:  # 짝수인 경우
                # 가능한 만큼 비트 시프트를 한 번에 처리
                shift = (num & -num).bit_length() - 1
                num >>= shift
                cnt += shift - 1  # 여러 비트를 한 번에 시프트한 만큼 횟수 조정
            cnt += 1
        return cnt


OtherSolution().numberOfSteps(14)
