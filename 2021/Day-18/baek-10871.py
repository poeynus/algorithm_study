n, x = map(int, input().split())

s_list = list(map(int, input().split()))
for i in s_list:
    if i < x:
        print(i, end=" ")