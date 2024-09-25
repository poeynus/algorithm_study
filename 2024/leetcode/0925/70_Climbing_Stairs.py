class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def fibonacci(s: int):
            if s <= 1:
                return 1

            if memo[s] != -1:
                return memo[s]

            memo[s] = fibonacci(s - 1) + fibonacci(s - 2)
            return memo[s]

        return fibonacci(n)


class GPTSolution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        # DP 배열 생성
        dp = [0] * (n + 1)
        dp[0] = 1  # 0번째 계단 (기본)
        dp[1] = 1  # 1번째 계단 (한 가지 방법)

        # 반복문을 통해 계단 수 계산
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # i번째 계단에 도달하는 방법

        return dp[n]  # n번째 계단에 도달하는 방법 반환


Solution().climbStairs(5)


# GPT는 DP 방법도 알려줌
