def my():
    card = [x for x in range(1, 21)]
    
    for _ in range(10):
        a, b = map(int, input().split())
        tmp = list(reversed(card[a-1:b]))
        
        for i in range(len(tmp)):
            card[a+i-1] = tmp[i]

    print(card)

def solution():
    a=list(range(21))
    for _ in range(10):
        s, e=map(int,input().split())
        for i in range((e-s+1)//2):
            a[s+i], a[e-i] = a[e-i], a[s+1]
    print(a)

my()


# 구간 a, b 정해자면 해당 구간 위치를 거꾸로 회전
# 또 주어지며 해당 구간 거꾸로
# 입력은 무조건 10개로 고정
# 입력 오면 그냥 해당 위치 문자열로 회전하면 되지 않을까