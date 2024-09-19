class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]


class OtherSolution:
    def addBinary(self, a: str, b: str) -> str:
        # 두 이진 문자열을 뒤집어서 처리
        a = a[::-1]
        b = b[::-1]

        # 결과를 저장할 리스트와 carry 초기화
        result = []
        carry = 0

        # 가장 긴 문자열의 길이만큼 반복
        max_length = max(len(a), len(b))
        for i in range(max_length):
            # 각 자리의 비트를 가져오기 (없으면 0)
            bit_a = int(a[i]) if i < len(a) else 0
            bit_b = int(b[i]) if i < len(b) else 0

            # 현재 자리의 덧셈과 carry 계산
            total = bit_a + bit_b + carry
            result.append(total % 2)  # 현재 자리의 비트
            carry = total // 2  # 새로운 carry

        # 마지막 carry가 남아있다면 추가
        if carry:
            result.append(carry)

        # 결과를 뒤집어서 문자열로 변환
        return "".join(str(x) for x in result[::-1])


Solution().addBinary("1010", "1011")


# Input: a = "11", b = "1"
# Output: "100"
#
# Input: a = "1010", b = "1011"
# Output: "10101"
