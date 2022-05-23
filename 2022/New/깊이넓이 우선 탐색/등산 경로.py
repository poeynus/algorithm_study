cnt = 0
def my():
  n = int(input())
  m = [list(map(int, input().split())) for _ in range(n)]
  chk = [[0] * n for _ in range(n)]

  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  
  low_m = min(map(min, m))
  high_m = max(map(max, m))

  low_list = [(i,j) for i in range(n) for j in range(n) if m[i][j] == low_m]
  high_list = [(i,j) for i in range(n) for j in range(n) if m[i][j] == high_m]
  chk[low_list[0][0]][low_list[0][1]] = 1

  def dfs(x, y):
    global cnt
    if x == high_list[0][0] and y == high_list[0][1]: 
      cnt += 1
    else:
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and m[nx][ny] > m[x][y] and chk[nx][ny] == 0:
          chk[nx][ny] = 1
          dfs(nx, ny)
          chk[nx][ny] = 0
  dfs(low_list[0][0], low_list[0][1])
  print(cnt)
my()

# 캬 파이썬이 좋긴 좋구나