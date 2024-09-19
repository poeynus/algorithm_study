class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split(" ")
        return len(s[-1])


class OtherSolution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                return len(s) - i - 1
        return len(s)


OtherSolution().lengthOfLastWord(" a")

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
