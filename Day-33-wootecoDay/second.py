def solution(log):
    answer = ''
    df = ''
    tmp = []
    cnt = 0
    for i in log:
        tmp.append(i.split(":"))

    c = [tmp[i] for i in range(len(tmp)) if i % 2 == 0]
    d = [tmp[i] for i in range(len(tmp)) if i % 2 != 0]

    for a, b in zip(c, d):
        h = int(b[0]) - int(a[0])
        m = int(b[1]) - int(a[1])
        if h > 0 and m < 0:
            h -= 1
            m + 60
        t = h * 60 + abs(m)

        if t <= 4 :
            t = 0 
        if t >= 105:
            t = 105 

        cnt += t 

    if cnt // 60 < 10:
        df = "0" + str(cnt//60)
    answer = df + ":" + str(cnt%60)
    
    return answer

solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"])

# ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]	"02:20"
# ["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]	"02:44"
# 40분 컷 ㅈ됬다.