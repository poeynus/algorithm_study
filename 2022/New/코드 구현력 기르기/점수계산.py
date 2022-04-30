def my():
    n = int(input())
    score_list = list(map(int, input().split()))
    result = 0
    cnt = 0

    for i in score_list:
        if i == 1:
            cnt += 1
            result += cnt
        elif i == 0:
            cnt = 0
    print(result)

def solution():
    pass
    # 이번엔 강사님이랑 완전 똑같아서 pass

my()

# 첫째 줄은 문제의 개수 둘째 줄은 1또는 0 0은 틀림 1은 맞음

# 일단 입력 받고 cnt로 하나씩 세면서 별도의 배열에 저장? 배열 쓰지말고 풀어볼까?
# 1나오면 cnt를 + 1 하고 cnt 값을 result에 저장
# 또 1나요면 cnt + 1 하고 cnt 값 저장
# 0 나오면 cnt = 0

# 배열 안쓰고 풀었다 요시