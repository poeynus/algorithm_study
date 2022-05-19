from collections import deque
# 섹션 3에서 이미 풀었었음 그때는 좌표 3개를 그냥 꽂고 풀이
def my():
  n = int(input())
  apple = [list(map(int, input().split())) for _ in range(n)]
  center = n//2
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  result = apple[center][center]
  dq = deque()
  dq.append((center, center))
  chk = [[0] * n for _ in range(n)]
  chk[center][center] = 1
  d = 0

  while True:
    if d == n//2:
      break
    size = len(dq)
    for _ in range(size):
      x,y = dq.popleft()
      for j in range(4):
        if chk[x+dx[j]][y+dy[j]] == 0:
          chk[x+dx[j]][y+dy[j]] = 1
          result += apple[x+dx[j]][y+dy[j]]
          dq.append((x+dx[j], y+dy[j]))
    d += 1
  print(result)

my()

# 중심좌표를 시작점으로 잡기
# 상하좌우로 돌리면서 더하기, 만약 이미 더한 위치라면 제거
# 끝에 닿을때까지만 하기
# 약간 꼬였네