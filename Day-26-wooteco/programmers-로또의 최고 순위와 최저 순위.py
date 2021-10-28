def solution(lottos, win_nums):
    answer = []
    result = [6, 6, 5, 4, 3, 2, 1]
    z_cnt = lottos.count(0)
    r_cnt = 0

    for i in lottos:
        if i in win_nums:
            r_cnt += 1

    answer.append(result[z_cnt+r_cnt])
    answer.append(result[r_cnt])

    return answer

# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
# [0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
# [45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]