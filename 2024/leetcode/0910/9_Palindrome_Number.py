class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        if len(x) & 1:
            mid = len(x) // 2
            x_list = list(x[:mid])
            x_list.reverse()
            if "".join(x_list) == x[mid + 1 :]:
                return True
            return False
        else:
            x_list = list(str(x))
            x_list.reverse()
            if "".join(x_list) == str(x):
                return True
            return False


class GPTSolution:
    def isPalindrome(self, x: int) -> bool:
        # 음수나 10의 배수(10, 100 등)는 회문이 아님
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # 회문 조건: x가 원래 숫자의 반절, reversed_half가 나머지 반절
        return x == reversed_half or x == reversed_half // 10


Solution().isPalindrome(12344321)
