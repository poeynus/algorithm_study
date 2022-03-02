def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] in answer:
            if answer[-1] != arr[i]:
                answer.append(arr[i])
        else:
            answer.append(arr[i])
    return answer
solution([4,4,4,3,3]	)
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	[4,3]