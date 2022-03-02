def solution(prices):

    answer = []

    for i in range(len(prices)):
        count = 1

        if i == len(prices)-1:
            answer.append(0)
        else:
            j = 1
            while prices[i] <= prices[i+j]:
                count+=1
                j+=1
                if i+j == len(prices):
                    count -= 1
                    break
            
            answer.append(count)
    return answer

# 다른 사람이 스택으로 짠 효율성 높은 코드
def a_solution(prices):
    answer = [0]*len(prices)
    stack = []
 
    for i, price in enumerate(prices):
        #stack이 비었이면 false
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
 
    # for문 다 돌고 Stack에 남아있는 값들 pop
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
 
    return answer


