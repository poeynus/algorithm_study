def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            answer = True
        else:
            answer =  False
    else:
        answer = False 
    return answer

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
    
solution("a123")
# "a234"	false
# "1234"	true