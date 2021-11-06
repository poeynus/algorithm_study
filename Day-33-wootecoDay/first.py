def solution(arr):
    answer = []
    tmp = []

    for i in range(1, 4):
        tmp.append(arr.count(i))
    
    for i in tmp:
        answer.append(max(tmp) - i)
    
    return answer

solution([1, 2, 3])

# [2, 1, 3, 1, 2, 1]	[0, 1, 2]
# [3, 3, 3, 3, 3, 3]	[6, 6, 0]
# [1, 2, 3]	     [0, 0, 0]
# 8분 컷