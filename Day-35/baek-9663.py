def check(x): 
    for i in range(x): 
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i: 
            return False 
    return True

def dfs(x):
    global result
 
    if x == n:
        result += 1
        return
    else:
        for i in range(n): 
            row[x] = i
            if check(x): 
                dfs(x + 1)
 
n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)

# 아 pypy3 말고 python으로는 어떻게 푸는거지
# 밑에꺼는 왜 안됨?
# 파이썬으로는 백트래킹 하면 안되네