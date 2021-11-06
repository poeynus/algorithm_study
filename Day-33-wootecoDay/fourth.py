def solution(s):
    answer = []
    cnt = 0
    s = list(s)
    
    for _ in range(len(s)):
        if s[0] == s[-1]:
            s.append(s[0])
            del s[0]

    for i in range(len(s)):
        cnt += 1
        if i == len(s)-1:
            answer.append(cnt)
            break
        if s[i] != s[i+1]:
            answer.append(cnt)
            cnt = 0
    return sorted(answer)

solution("wowwow")

# "aaabbaaa"	[2,6]
# "wowwow"	[1,1,2,2]
# 2시간 10분 남았다.