import math

def my():
    n = int(input())
    prime_check = [0] * (n+1)

    for i in range(2, n+1):
        if prime_check[i] != 1:
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    break
                else:
                    prime_check[i] = 1

    print(prime_check)


def solution(): 
    n = int(input())
    ch = [0] * (n+1)
    cnt=0
    for i in range(2, n+1):
        if ch[i]==0:
            cnt+=1
            for j in range(i, n+1, i):
                ch[j] = 1
    print(cnt)

solution()

# 먼저 배열을 입력 값 만큼 생성
# 반복문 돌리기 2~입력 값
# 첫 번째 조건 배열의 값이 1이면 pass
# 아닐 경우 두 번째 조건 소수 이면 해당 위치 값 1로 변경
# 여기서 반복문 한 번더 배수들 전부 1로 변경

# 나는 처음 들어오는 값들 부터 소수인지 아닌지 판별하고 계산하려고 했는데 그럴 필요가 없었네
# 내가 너무 어렵게 생각했다. 다시 해야겠다.