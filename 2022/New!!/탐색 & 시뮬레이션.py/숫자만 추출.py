import math

def my():
    word = list(input())
    result = ''
    cnt = 0
    check = 0
    for i in word:
        if i.isdigit():
            result += i
    
    result = int(result)

    for i in range(1,int(math.sqrt(result)+1)):
        if result % i == 0:
            if result // i == i:
                check += 1
            cnt += 1 
    print(result)
    print(cnt * 2 - check)

def solution():
    s=input()
    res=0
    for x in s:
        if x.isdecimal():
            res=res*10+int(x)
    print(res)
    cnt = 0
    for i in range(1, res+1):
        if res%i == 0:
            cnt += 1
    print(cnt)

my()

# 첫줄 숫자문자 섞인 문자열
# 첫줄에 자연수 둘째 둘에 약수의 개수

# 입력 받고 문자열 하나하나 isdigit으로 비교 후 저장
# 이거 int로 숫자로 변환
# 약수 구해서 출력

# 나는 별도의 라이브러리를 썼다.