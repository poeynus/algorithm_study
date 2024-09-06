class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for i in list(ransomNote):
            if i in magazine:
                magazine = magazine.replace(i, "", 1)
            else:
                return False
        return True


class GPTSolution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # magazine의 각 문자 빈도수를 세는 딕셔너리
        magazine_count = {}

        # magazine의 문자 빈도수 기록
        for char in magazine:
            magazine_count[char] = magazine_count.get(char, 0) + 1

        # ransomNote의 문자 빈도수를 확인
        for char in ransomNote:
            if magazine_count.get(char, 0) <= 0:
                return False
            magazine_count[char] -= 1

        return True


# 딕셔너리를 애용해야 겠다. - 생각해보니 자바에서도 일 할 때 map을 많이 써서 성능 향상 시켰었는데...

Solution().canConstruct("aab", "ba")
GPTSolution().canConstruct("aab", "ba")
