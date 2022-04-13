def my():
    n = int(input())
    result = []

    for _ in range(n):
        a = list(map(int, input().split()))

        if(a[0] == a[1] and a[1] == a[2]):
            result.append(10000 + (a[0] * 1000))
        elif(a[0] == a[1] and a[1] != a[2]):
            result.append(1000 + (a[0] * 100))
        elif(a[0] != a[1] and a[1] == a[2]):
            result.append(1000 + (a[1] * 100))
        elif(a[0] == a[2] and a[2] != a[1]):
            result.append(1000 + (a[0] * 100))    
        else:
            result.append(max(a) * 100)
    print(max(result))

def solution():
    n = int(input())
    for i in range(n):
        tmp=input().split()
        tmp.sort()
        a, b, c = map(int, tmp)
        if a == b and b == c:
            money=10000+1*1000
        elif a == b or a == c:
            money=1000+(a*100)
        elif b == c:
            money=1000+(b*100)
        else:
            money=c*100

        if money>res:
            res=money
    print(res)

my()

# 같은 눈 3개 = 나오면 10000 + 눈의 수 * 1000
# 같은 눈 2개 = 1000 + 눈의 수 * 100
# 모두 다른 눈 = 가장 큰 눈의 수 * 100

# 첫째 줄 참여하는 사람 수
# 사람들이 주사위를 던진 3개의 눈
# 출력은 가장 많은 상금을 받은 사람의 상금

# 나도 간단한 문제에서는 배열을 사용하지 않고 푸는 쪽으로 연습해야겠다.