def solution(answers):
    answer = []
    f_man = [1,2,3,4,5] * 2000
    s_man = [2,1,2,3,2,4,2,5] * 1250
    t_man = [3,3,1,1,2,2,4,4,5,5] * 1000

    f_cnt = 0
    s_cnt = 0
    t_cnt = 0

    for a, b, c, d in zip(answers, f_man, s_man, t_man):
        if a == b:
            f_cnt += 1
        if a == c:
            s_cnt += 1
        if a == d:
            t_cnt += 1

    if f_cnt > s_cnt and f_cnt > t_cnt:
        answer.append(1)
    elif s_cnt > f_cnt and s_cnt > t_cnt:
        answer.append(2)
    elif t_cnt > f_cnt and t_cnt > s_cnt:
        answer.append(3)
    elif f_cnt > t_cnt and f_cnt == s_cnt:
        answer.append(1)
        answer.append(2)
    elif f_cnt > s_cnt and f_cnt == t_cnt:
        answer.append(1)
        answer.append(3)
    elif s_cnt > f_cnt and s_cnt == t_cnt:
        answer.append(2)
        answer.append(3)
    elif f_cnt == s_cnt and s_cnt == t_cnt:
        answer.append(1)
        answer.append(2)
        answer.append(3)
    
    return answer

solution([1,2,3,4,5])

# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]