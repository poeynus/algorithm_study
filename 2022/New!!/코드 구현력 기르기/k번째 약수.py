from math import sqrt

def my():
    n, k = map(int, input().split())

    result = []

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                result.append(i)
            else:
                result.append(i)
                result.append(n // i)

    result.sort()

    if k > len(result):
        print(-1)
    else:
        print(result[k-1])


def solution():
    n, k = map(int, input().split())
    cnt=0
    for i in range(1, n+1):
        if n%i==0:
            cnt+=1
        if cnt==k:
            print(i)
            break
    else:
        print(-1)


# 6 3
# 3

# k번째 약수
# n을 루트 연산 + 1 까지 나누기 해서 0 나오면 배열안에 나누는 값과 몫 넣기
# 조건문 으로 나누는 값과 나눠진 값이 같으면 나누는 값만 넣기
# 정렬 후 해당 인덱스 출력
# 1 16 2 8 4
