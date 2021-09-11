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

solution([1, 2, 3, 2, 3]) # 4 3 1 1 0
