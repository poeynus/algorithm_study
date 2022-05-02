import math

def solution(fees, records):
    answer = dict()
    chk = dict()
    result = []

    for i in records:
        if i[11:] == 'IN':
            hour = int(i[0:2]) * 60
            minute = int(i[3:5])
            answer[i[6:10]] = (answer.get(i[6:10]) or 0) + hour + minute
            chk[i[6:10]] = True
        else:
            hour = int(i[0:2]) * 60
            minute = int(i[3:5])
            answer[i[6:10]] = answer.get(i[6:10]) - (hour + minute)
            chk[i[6:10]] = False

    for key, value in chk.items():
        if value == True:
            hour = 23 * 60
            minute = 59
            answer[key] = answer.get(key) - (hour + minute)
        answer[key] = -answer.get(key)

    for key, value in answer.items():
        if value <= fees[0]:
            answer[key] = fees[1]
        else:
            answer[key] = fees[1] + math.ceil((value - fees[0]) / fees[2]) * fees[3]
    
    answer = sorted(answer.items(), key = lambda item: int(item[0]))



    for key, value in answer:
        result.append(value)

    return result

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])

# 입력 값들을 잘 사용 해서 {차량번호 : 시간} 형태로 바꿀 수 있을라나
# IN 이면 {차량번호 : 시간} 등록 OUT 이면 {차량번호 : 시간 - 입력 시간}

# 와 요즘 알고리즘 한 효과가 있나
# 벽이라 생각 했었던 카카오 문제를 풀었다