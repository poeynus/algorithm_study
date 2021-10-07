def solution(priorities, location):

    where = [x for x in range(len(priorities))]

    result = []

    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            result.append(where.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            where.append(where.pop(0))

    answer = result.index(location) + 1

    return answer



solution([2, 1, 3, 2], 2)
