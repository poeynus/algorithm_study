
def solution(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        print(n, mod)
        rev_base += str(mod)
    
    return int(rev_base, 3)

solution(45)

# 45	7
# 125	229