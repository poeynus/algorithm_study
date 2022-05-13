cnt = 0

def my():
  n, m = map(int, input().split())
  hang = [[0] * (n+1) for _ in range(m+1)]
  ch = [0] * (n+1)
  ch[1] = 1

  for _ in range(m):
    h, y = map(int, input().split())
    hang[h][y] = 1

  # d = depth
  def dfs(d):
    global cnt
    if d == n:
      cnt += 1
    else:
      for i in range(1, n+1):
        if hang[d][i] == 1 and ch[i] == 0:
          ch[i] = 1
          dfs(i)
          ch[i]= 0
  
  dfs(1)
  print(cnt)
  
my()