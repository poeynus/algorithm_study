from itertools import combinations
import math

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    num_list = list(combinations(nums, 3))
    for i in num_list:
        sosu = i[0] + i[1] + i[2] 
        if is_prime_num(sosu) == True:
            answer += 1
            
    return answer

