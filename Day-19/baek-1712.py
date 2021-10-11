a, b, c = map(int, input().split())

count = 1

if b > c or b == c:
    print(-1)
else:
    print(int(a / (c - b)) + 1)
