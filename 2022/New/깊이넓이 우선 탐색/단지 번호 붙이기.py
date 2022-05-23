cnt = 0
def my():
  global cnt
  n = int(input())
  m = [list(map(int, input())) for _ in range(n)]
  result = []
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]

  def dfs(x, y):
    global cnt
    m[x][y] = 0
    cnt += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and m[nx][ny] == 1:
        dfs(nx, ny)

  for i in range(n):
    for j in range(n):
      if m[i][j] == 1:
        cnt = 0
        dfs(i, j)
        result.append(cnt)
  result.sort()
  print(len(result))
  for i in result:
    print(i)
my()