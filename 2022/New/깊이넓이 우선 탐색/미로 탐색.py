cnt = 0
def my():
  miro = [list(map(int, input().split())) for _ in range(7)]
  miro[0][0] = 1
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]

  def dfs(x, y):
    global cnt
    if x == 6 and y == 6:
      cnt += 1
    else:
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 7 and 0 <= ny < 7 and miro[nx][ny] == 0:
          miro[nx][ny] = 1
          dfs(nx, ny)
          miro[nx][ny] = 0 

  dfs(0,0)
  print(cnt)

my()

# dfs, bfs도 할 만 하다.