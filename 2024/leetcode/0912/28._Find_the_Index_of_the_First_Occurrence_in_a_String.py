class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


Solution().strStr("sadbutsad", "sad")


class GPTSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP 알고리즘의 LPS 배열을 생성
        def computeLPS(pattern: str) -> list[int]:
            lps = [0] * len(pattern)
            length = 0  # 현재 LPS 길이
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # 패턴이 빈 문자열인 경우
        if not needle:
            return 0

        lps = computeLPS(needle)
        i = 0  # haystack의 인덱스
        j = 0  # needle의 인덱스

        while i < len(haystack):
            if needle[j] == haystack[i]:
                i += 1
                j += 1

            if j == len(needle):
                return i - j

            # 불일치 발생 시 LPS 배열을 활용
            elif i < len(haystack) and needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1


# python 이라서 걍 되는듯, KMP 알고리즘
