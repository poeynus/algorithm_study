def solution(rows, columns):
    answer = [[0] * columns for _ in range(rows)]
    r = 0
    c = 0
    n = 1

    if rows == columns:
        while True:
            if any(rows * 2 in i for i in answer):
                break
            answer[r][c] = n
            if n & 1: # 홀수
                c += 1
                if c == columns:
                    c = 0
            else:
                r += 1
                if r == rows:
                    r = 0
            n += 1
    else:
        while True:
            if not any(0 in i for i in answer):
                break
            answer[r][c] = n
            if n & 1: # 홀수
                c += 1
                if c == columns:
                    c = 0
            else:
                r += 1
                if r == rows:
                    r = 0
            n += 1

    return answer


solution(4, 4)

# 3	4	[[8,2,13,14],[16,10,4,15],[17,11,12,6]]
# 3	3	[[1,2,0],[0,3,4],[6,0,5]]