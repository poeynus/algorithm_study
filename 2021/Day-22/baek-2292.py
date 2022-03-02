n = int(input())

cnt = 1
c_n = 1

while n > c_n:
    c_n += cnt * 6
    cnt += 1

print(cnt)