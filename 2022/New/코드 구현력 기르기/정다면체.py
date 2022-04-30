def my():
    n, m = map(int, input().split())
    result = [0] * n * m

    for i in range(1, n+1):
        for j in range(1, m+1):
            result[i+j-1] += 1

    la = n if n < m else m
    for i in range(len(result)):
        if result[i] == la:
            print(i+1, end=" ")
 
def solution():
    n, m = map(int, input().split())
    cnt=[0]*(n+m+3)
    max = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            cnt[i+j] += 1 

    for i in range(n+m+1):
        if cnt[i]> max:
            max=cnt[i]

    for i in range(n+m+1):
        if cnt[i] == max:
            print(i, end=' ')
my()

# 좀 쉽게 풀었네