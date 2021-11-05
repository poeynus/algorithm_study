from itertools import permutations

def solution(numbers):
    answer = []
    calc = []

    for i in permutations(numbers, len(numbers)):
        calc.append(''.join(map(str, i)))

    for i in calc:
        answer.append(''.join(i))

    answer = list(map(int, answer))

    return str(max(answer))

solution([6, 10, 2])

# 시간 초과로 인한 실패 이제 람다를 쓸 줄 알아야 한다.
#     [6, 10, 2]	"6210"
# [3, 30, 34, 5, 9]	"9534330"