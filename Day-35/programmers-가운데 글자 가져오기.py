def solution(s):
    answer = ''
    if len(s) & 1:
        answer = s[int(len(s) / 2)]
    else:
        answer = s[int(len(s) / 2 - 1) : int(len(s) / 2 + 1)]
    return answer
solution("qwer")
# "abcde"	"c"
# "qwer"	"we"