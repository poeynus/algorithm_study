def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    
    if answer:
        answer.sort()
    else:
        answer.append(-1)

    return answer

def hot(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
# [5, 9, 7, 10]	5	[5, 10]
# [2, 36, 1, 3]	1	[1, 2, 3, 36]
# [3,2,6]	10	[-1]