n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
result = []

for p, q in zip(a, b):
    tmp = []
    for d, e in zip(p, q):
        tmp.append(d+e)
    result.append(tmp)

for i in result:
    for j in i:
        print(j, end=" ")
    print()