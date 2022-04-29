from itertools import combinations
import time

def my():
    start = time.time()
    n, k = map(int, input().split())
    in_list = list(map(int, input().split()))
    com_list = []

    for i in combinations(in_list, 3):
        com_list.append(sum(i))

    result_list = list(set(com_list))
    result_list.sort(reverse=True)

    print(result_list[k-1])
    print(time.time() - start)

def soulution():
    start = time.time()
    # n개의 정수와 K번째 큰 값을 가져온다.
    n, k =map(int, input().split())
    # n개의 리스트를 리스트형식으로 가져온다.
    a=list(map(int,input().split()))
    
    res=[]
    
    # 3중 for문 : 주어진 배열에서 3개를 뽑는 경우의 수 구현
    for i in range(n):
        for j in range(i+1,n):
            for m in range(j+1,n):
                # 중복을 제거하면 res에 입력
                res.append(a[i]+a[j]+a[m])
    
    # 중복을 제거하는 자료구조 : set()
    # res를 list화 시켜서 sort사용(내림차순 정렬)
    res=list(set(res))
    res.sort(reverse=True)
    # k번째 추출
    print(res[k-1])
    print(time.time() - start)

soulution()