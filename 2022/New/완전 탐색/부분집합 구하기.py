def dfs(x):
  if x == 4:
    for i in range(1, len(chk)):
      if chk[i] == 1:
        print(i, end=' ')
    print()
  
  else:
    chk[x] = 1
    dfs(x)
    chk[x] = 0
    dfs(x)

n = int(input())
chk = [0] * (n + 1)

dfs(1)

# dfs쓰는데 쓴다 안쓴다 2가지로 돌리면 가능하다.
# 입력 받고 계속 dfs로 보내

# 이거로 다시 짜본다