def solution(nums):
    answer = 0
    tmp = set(nums)

    if len(tmp) > len(nums) / 2:
        answer = int(len(nums) / 2)
    else:
        answer = len(tmp)
    
    return answer

def hot(ls):
    return min(len(ls)/2, len(set(ls)))
    
solution([3,1,2,3])

# [3,1,2,3]	2
# [3,3,3,2,2,4]	3
# [3,3,3,2,2,2]	2