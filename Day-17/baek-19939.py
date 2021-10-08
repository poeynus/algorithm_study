n, k = map(int, input().split())

k_list = [x for x in range(1,k+1)]

if(sum(k_list) > n):
    print(-1)
elif((sum(k_list)-n) % k == 0):
    print(k-1)
else:
    print(k)