import math

def my():
    n = int(input())
    in_list= list(input().split())

    for i in in_list:
        re_int = reverse(i)
        if isPrime(re_int):
            print(re_int, end=' ')

def reverse(x):
    return int(x[::-1])

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    for x in a:
        tmp=so_reverse(x)
        if isPrime(tmp):
            print(tmp, end=' ')

def so_reverse(x):
    res = 0
    while x > 0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def so_isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    else:
        return True

my()

# 이 문제는 강사님 풀이보다 내가 한 풀이가 더 재미있게 된 듯?