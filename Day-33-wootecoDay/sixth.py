def solution(time, plans):
    answer = ''
    work = [[13, 18], [9, 18]]
    cnt = 0

    for i in plans:
        if "PM" in i[1]:
            i[1] = i[1].replace("PM", "")
            i[1] = int(i[1]) + 12
        elif "AM" in i[1]:
            i[1] = i[1].replace("AM", "")
            i[1] = int(i[1])

        if "PM" in i[2]:
            i[2] = i[2].replace("PM", "")
            i[2] = int(i[2]) + 12
        elif "AM" in i[2]:
            i[2] = i[2].replace("AM", "")
            i[2] = int(i[2])

        if i[1] >= work[1][1]:
            pass
        if i[2] <= work[0][0]:
            pass
        if i[2] > work[0][0]:
            cnt += i[2] - work[0][0] 
        if i[1] < work[1][0]:
            cnt += i[1] - work[0][0]

        print(cnt)
    print(work)
    
    
    return answer

solution(3.5, [ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ])

# 3.5	[ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]	"홍콩"
# da    db
# 13:00 18:00

# ca   cb
# 9:30 18:00

# a     b
# 23:00 9:00 
# 15:00 14:00

# 12시간제를 24시간제로 바꾸고 하나하나 비교 하기

# a가 ca보다 작으면 휴가 써야 함 - 필요 없는 조건 인 거 같다.
# a가 ca보다 크고 cb보다 작을 경우 휴가 써야함 

# a가 cb보다 크면 그냥 pass
# b가 da보다 작으면 그냥 pass

# b가 da보다 크면 휴가 써야 함