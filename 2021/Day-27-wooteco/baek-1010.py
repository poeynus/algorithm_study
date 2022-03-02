import math

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    perm = 1

    for i in range(m, m-n, -1):
        perm *= i

    print(int(perm / math.factorial(n)))
