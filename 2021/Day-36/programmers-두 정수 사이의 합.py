def solution(a, b):
    answer = 0
    if a > b:
        for i in range(b, a+1):
            answer += i
    else:
        for i in range(a, b+1):
            answer += i

    return answer

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2
# 3	5	12
# 3	3	3
# 5	3	12