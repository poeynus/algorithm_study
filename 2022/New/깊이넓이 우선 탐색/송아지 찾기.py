from collections import deque

def my():
  s, e = map(int, input().split())
  MAX = 10000
  dis = [0] * (MAX+1) # 몇번 만에 해당 거리 도착하는지 저장
  chk = [0] * (MAX+1) # 중복 체크
  chk[s] = 1
  dq = deque()
  dq.append(s)

  while dq:
    n = dq.popleft()
    if n == e:
      print(dis[n])
      break
    for m in(n-1, n+1, n+5):
      if 0 < m <= MAX and chk[m] == 0:
        dq.append(m)
        dis[m] = dis[n]+1
        chk[m] = 1

 

my()

# 입력 받고 한 번에 갈 수 있는 경우의 수를 전부 queue에 삽입
# 목표에 도달할 때 까지 진행, 만약 이미 들어간 값이 있으면 제외

# bfs 안 익숙해서 dfs처럼 풀었네 다시 풀었음
# bfs는 데크로 푸는게 편한 거 같다. 리스트로 해도 상관 없는듯