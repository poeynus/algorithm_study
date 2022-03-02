def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer
    
solution([4,7,12], [True, False, True])

# [4,7,12]	[true,false,true]	9
# [1,2,3]	[false,false,true]	0