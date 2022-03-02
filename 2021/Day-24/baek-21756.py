n = int(input())

if n == 1:
    print(n)
else:
    n_list = [x for x in range(2, n+1, 2)]

    while len(n_list) != 1:
        n_list = n_list[1::2]
    
    print(n_list[0])   