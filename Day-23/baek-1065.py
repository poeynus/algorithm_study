n = int(input())

cnt = 0

if n < 99:
    print(n)
else:
    cnt += 99
    t_list = [x for x in range(99, n+1)]
    del t_list[0]
    for i in t_list:
        i = str(i)
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            cnt += 1
    print(cnt)