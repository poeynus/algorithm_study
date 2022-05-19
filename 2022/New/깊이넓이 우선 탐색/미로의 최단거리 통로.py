from collections import deque

def my():
  miro = [list(map(int, input().split())) for _ in range(7)]
  miro[0][0] = 1
  dis = [[0] * 7 for _ in range(7)]
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  dq = deque()
  dq.append((0,0))

  while dq:
    ox, oy = dq.popleft()
    for i in range(4):
      x = ox + dx[i]
      y = oy + dy[i]
      if 0 <= x < 7 and 0 <= y < 7 and miro[x][y] == 0:
        miro[x][y] = 1
        dis[x][y] = dis[ox][oy] + 1
        dq.append((x,y))
        
  if dis[6][6] == 0:
    print(-1)
  else:
    print(dis[6][6])

my()

# 이거 풀면서 의문이 생긴게 여러가지 길이 나올경우 마지막으로 들어간 값이 어떻게 최단경로가 되는건지 궁금했다.
# 큐를 이용한 탐색은 어떤 지점에 제일 먼저 도착하는 것이 최단거리로 가게 되어있다고 한다. 
# 그니까 별도로 분기를 안만들어줘도 된다고 한다. 처음에는 비교하는 값을 만들어 줬었는데 필요 없다고 한다.