from collections import deque

def my():
  n = int(input())
  m = [list(map(int, input().split())) for _ in range(n)]
  dx = [-1, -1, 0, 1, 1, 1, 0, -1]
  dy = [0, 1, 1, 1, 0, -1, -1, -1]
  cnt = 0
  dq = deque()

  for i in range(n):
    for j in range(n):
      if m[i][j] == 1:
        m[i][j] = 0
        dq.append((i,j))
        while dq:
          ox, oy = dq.popleft()
          for k in range(8):
            x = ox + dx[k]
            y = oy + dy[k]
            if 0 <= x < n and 0 <= y < n and m[x][y] == 1:
              m[x][y] = 0
              dq.append(x, y)
        cnt += 1
  print(cnt)
my()