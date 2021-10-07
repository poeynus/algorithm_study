tc = int(input())

for _ in range(tc):
    docu_num, where = map(int, input().split())
    docu_list = list(map(int, input().split()))

    index = [x for x in range(len(docu_list))]

    result = []

    while docu_list:
        if docu_list[0] == max(docu_list):
            docu_list.pop(0)
            result.append(index.pop(0))
        else:
            docu_list.append(docu_list.pop(0))
            index.append(index.pop(0))

    print(result.index(where) + 1)