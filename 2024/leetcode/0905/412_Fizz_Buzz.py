from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [
            (
                "FizzBuzz"
                if i % 15 == 0
                else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)
            )
            for i in range(1, n + 1)
        ]


class GPTSolution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            output = ""
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            if not output:
                output = str(i)
            result.append(output)
        return result


# 단순 숫자를 바꾸는 경우 f"{i}" < str(i)

# str() 함수는 숫자를 문자열로 변환하는 데 최적화된 내장 함수입니다.
# 단순히 숫자를 문자열로 변환할 때 가장 빠르고 효율적인 방법입니다.

# f"{i}"는 포맷 문자열을 사용하여 값을 삽입하는 방식입니다.
# 이 방법은 내부적으로 str()을 호출하긴 하지만, 포맷팅을 지원하기 때문에 약간의 오버헤드가 발생할 수 있습니다.
# 특히 복잡한 포맷팅이 필요한 경우에는 더 많은 오버헤드가 발생합니다.
