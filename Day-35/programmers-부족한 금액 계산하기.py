def solution(price, money, count):
    result = 0
    answer = 0
    for i in range(1, count+1):
        result = result + (i * price)
        
    if money >= result :
        answer = 0
    else:
        answer = result - money
    
    return answer

solution(3, 20, 4)
# 3 20 4 10