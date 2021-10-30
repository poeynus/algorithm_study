def solution(left, right):
    n_list = [x for x in range(left, right+1)]
    even_divisor = 0

    for i in n_list:
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            even_divisor += i
    
    odd_divisor = sum(n_list) - even_divisor
    answer = even_divisor - odd_divisor
    
    return answer

solution(24, 27)
# 13	17	43
# 24	27	52