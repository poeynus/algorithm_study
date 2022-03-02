n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = 0

for _ in range(n):
    result = result + (max(a) * min(b))
    a.remove(max(a))
    b.remove(min(b))

print(result)

def sec():
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0

    a.sort()
    b.sort(reverse=True)

    for i in range(n):
        result = result + (a[i] * b[i])

    print(result)



# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# 5
# 1 1 1 6 0       A만 재배열 가능
# 2 7 8 3 1     18