def my():
    n = int(input())
    in_list = list(input().split())
    result = []
    a = [] # 값이 동일할 때 가장 큰 값

    for i in in_list:
        tmp = list(map(int, i))
        result.append(sum(tmp))
        
    for i in range(len(result)):
        bi = max(result)
        if result[i] >= bi:
            print(in_list[i])
            break
    #     if result[i] >= bi:    # 이거는 값이 동일할 때 가장 큰 값 출력하게끔 구성
    #         a.append(in_list[i])

    # print(max(a))

def solution():
    n=int(input())
    a=list(map(int, input().split()))
    max = -2147000000
    for x in a:
        tot = digit_sum(x)
        if tot>max:
            max=tot
            res=x
    print(res)

def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum
my()

# 각 자릿수 더하면 되네
# 걍 스트링으로 입력 받고 반복문 돌려서 하면 되지 않을까
# 문제가 값이 똑같을 경우가 적용이 안되어 있네.
