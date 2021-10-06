n = int(input())
count = 0
t = n

while True:
    count += 1
    a = t // 10
    b = t % 10
    c = a + b
    t = (b * 10) + (c % 10)

    if(n == t):
        break

print(count)