class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1

        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            elif sq > x:
                right = mid - 1
        return left - 1


class GPTSolution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        # 초기값은 x 또는 적절한 수 (x/2 혹은 1로 시작 가능)
        y = x
        while True:
            new_y = (y + x / y) / 2
            # 원하는 정확도 (0.00001 이하로 근사할 때까지 반복)
            if abs(y - new_y) < 0.00001:
                break
            y = new_y

        return int(y)  # 정수 부분만 반환


# GPT는 뉴턴 랩슨 방법도 알려주네

Solution().mySqrt(2147395599)
