import datetime

def solution(a, b):
    answer = datetime.datetime(2016, a, b)
    
    return answer.strftime('%a').upper()

solution(5, 24)
# 5	24	"TUE"