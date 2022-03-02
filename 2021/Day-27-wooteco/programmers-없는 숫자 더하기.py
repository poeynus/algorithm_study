def solution(numbers):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0

    for i in num:
        if i in numbers:
            pass
        else:
            answer += i

    return answer

def hot(numbers):
    return 45 - sum(numbers)

solution([5,8,4,0,6,7,9])

# [1,2,3,4,6,7,8,0]	14
# [5,8,4,0,6,7,9]	6