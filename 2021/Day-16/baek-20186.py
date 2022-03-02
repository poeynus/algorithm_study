n, k = map(int, input().split())
n_list = list(map(int, input().split()))

data_list = n_list
max_list = []
result = 0

if k == 1:
    print(max(data_list))
else:
    for i in range(k):
        a = max(data_list)
        b = data_list.index(a)
        data_list[b] = 0
        max_list.append(a)
    result = sum(max_list)
    result = int(result - (k * (k+1) / 2 - k))
    print(result)