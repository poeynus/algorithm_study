s = int(input())

result = 0

while s >= 0:
    if s % 5 == 0:
        result += s //5
        print(result)
        break
    s -= 3
    result += 1

else:
    print(-1)
