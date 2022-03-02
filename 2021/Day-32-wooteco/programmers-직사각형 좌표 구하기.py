def solution(v):
    answer = []
    x = [i[0] for i in v]
    y = [i[1] for i in v]

    for i in x:
        cnt = 0
        cnt = x.count(i)
        if cnt == 1:
            answer.append(i)
            break
    for i in y:
        cnt = 0
        cnt = y.count(i)
        if cnt == 1:
            answer.append(i)
            break

    return answer
solution([[1, 4], [3, 4], [3, 10]])

#     [[1, 4], [3, 4], [3, 10]]	[1, 10]
# [[1, 1], [2, 2], [1, 2]]	[2, 1]