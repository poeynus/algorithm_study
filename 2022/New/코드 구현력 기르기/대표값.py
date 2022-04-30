import math

def my():
    n = int(input())
    score_list = list(map(int, input().split()))
    result = []

    average = sum(score_list) / n    
    ave_check = sum(score_list) // n

    if(ave_check & 1): # 홀수
        average = round(average)
    else:
        if(average - ave_check < 0.5 ):
            average = math.trunc(average)
        else:
            average = math.ceil(average)
    
    for i in score_list:
        result.append(abs(average - i))

    print(result)
    

def solution():
    n = int(input())
    score_list = list(map(int, input().split()))
    ave = round(sum(score_list)/n)
    min = 2147000000
    for idx, x in enumerate(score_list):
        tmp=abs(x-ave)
        if tmp < min:
            min=tmp
            score=x
            res=idx+1
        elif tmp==min:
            if x>score:
                score=x
                res=idx+1

    print(ave, res)


my()

# 첫 줄 점수 개수 두 번째 줄 점수들 학생 번호는 앞에서 부터 1
# 평균 가까운 점수가 여러개일 경우 점수가 높은사람 5 > 4, 6 => 6이 답
# 점수 높은 사람이 여러명이면 번호가 빠른사람

# 아 짜증나네 나 왤케 어렵게 짜지
# 나는 모두 한번에 계산하고 나중에 검사하는 식으로 했고 강사님은 하나 하나 계산과 동시에 검사하는 방식

# 반올림 사사오입 문제에 막힌 당신에게 주는 풀이법
# https://blockdmask.tistory.com/112
# 62.5 이렇게 있으면 round쓰면 62가 나오는데 round를 쓰지말고
# 62.5에서 0.5를 더한 후 그냥 내림을 써라
# 62.4 + 0.5 = 62.9 내림 하면 62
# 62.6 + 0.5 = 63.1 내림 하면 63   
# 이런게 진짜 천재의 발상이네 알 깼다.