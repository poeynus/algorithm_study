from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_list = []
        for i in range(len(accounts)):
            sum_list.append(sum(accounts[i]))
        return max(sum_list)


class OtherSolution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for i in range(len(accounts)):
            accounts[i] = [sum(accounts[i])]
        return max(accounts)[0]


class GptSolution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # 각 사람의 자산 합계를 바로 계산하면서 최댓값을 업데이트합니다.
        return max(sum(account) for account in accounts)


Solution().maximumWealth([[1, 5], [7, 3], [3, 5]])
