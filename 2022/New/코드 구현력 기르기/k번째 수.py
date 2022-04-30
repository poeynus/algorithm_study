def my():
    tc = int(input())
    res = []
    for i in range(tc):
        n, s, e, k = map(int, input().split())
        some_list = list(map(int, input().split()))
        
        result = some_list[s-1:e]
        result.sort()
        res.append(result[k-1])
        
    for i in range(len(res)):
        print(f"#{i+1} {res[i]}")

def solution():
    T=int(input())
    for t in range(T):
        n, s, e, k = map(int, input().split())
        a=list(map(int,input().split()))
        a=a[s-1:e]
        a.sort()
        print("#%d %d" %(t+1, a[k-1]))
my()

# tc 입력
# n, s, e, k 입력
# 배열 값들

# tc 받고 반복문을 tc로 돌려서 n, s, e, k 분리 하고 배열 값들로 배열 생성
# 문자열 슬라이스로 s부터 e까지 자르고 sort한 후 k번째 수 출력