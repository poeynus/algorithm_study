from itertools import combinations

def solution(numbers):
    answer = []

    for i in combinations(numbers, 2):
        answer.append(sum(i))

    answer = sorted(list(set(answer)))
    
    return answer

solution([5,0,2,7])

# [2,1,3,4,1]	[2,3,4,5,6,7]
# [5,0,2,7]	[2,5,7,9,12]