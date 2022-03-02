def solution(d, budget):
    answer = 0
    result = 0

    for _ in range(len(d)):
        result += min(d)
        d.remove(min(d))
        answer += 1
        if result > budget:
            answer -= 1
            break
        if result == budget:
            break

    return answer

solution([1,3,2,5,4], 9)
solution([2,2,3,3],	10)
# [1,3,2,5,4]	9	3
# [2,2,3,3]	10	4

# 두 줄로 입력 받기 - d, b
# result, cnt 선언
# while result > b
# reulst += min(result)
# cnt += 1