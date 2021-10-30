def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += a[i] * b[i]
    
    return answer

def hot(a, b):

    return sum([x*y for x, y in zip(a,b)])

solution([1,2,3,4], [-3,-1,0,2])

# [1,2,3,4]	[-3,-1,0,2]	3
# [-1,0,1]	[1,0,-1]	-2