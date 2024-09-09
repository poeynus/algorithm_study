from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        profit = 0
        min_price = float("inf")
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]

            if prices[i] - min_price > profit:
                profit = prices[i] - min_price
                if i < len(prices) - 1:
                    if prices[i + 1] <= prices[i]:
                        result += profit
                        profit = 0
                        min_price = float("inf")
        result += profit
        return result


class GPTSolution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit


Solution().maxProfit([5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0])


# 아 이걸 내가 너무 복잡하게 생각했네
# 간단하게 풀 수 있었는데
