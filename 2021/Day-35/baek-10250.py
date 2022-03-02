tc = int(input())

for _ in range(tc):
    h, w, n = map(int, input().split())
    a = str(n // h + 1)
    b = str(n % h)

    if int(b) == 0:
        a = str(n // h)
        b = str(h)

    if int(a) < 10:
        a = "0" + a
    
    print(b + a)


# h, w, n입력 받기
# n을 h로 나누고 몫을 a, 나머지를 b
# 문자열 붙이기 b + (a+1) if a < 10: a =  0 + a