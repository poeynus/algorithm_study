from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for index, i in enumerate(prices):
            for j in prices[index:]:
                if j - i > max_profit:
                    max_profit = j - i
        return max_profit


class OtherSolution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for index, i in enumerate(prices):
            if i < min_price:
                min_price = i

            if i - min_price > max_profit:
                max_profit = i - min_price
        return max_profit


OtherSolution().maxProfit([7, 1, 5, 3, 6, 4])
