p = 0
def my():
  n = int(input())
  time = [0]
  score = [0]

  for _ in range(n):
    t, s = map(int,input().split())
    time.append(t)
    score.append(s)

  def dfs(d, s):
    global p 
    if d > n + 1:
      return
    if d == n + 1:
      if s > p:
        p = s
    else:
      dfs(d + time[d], s + score[d])
      dfs(d + 1, s)

  def ndfs(d,s):
    global p 
    if d == n + 1:
      if s > p:
        p = s
    else:
      if d + time[d] <= n + 1:
        dfs(d + time[d], s + score[d])
      dfs(d + 1, s)

  dfs(1, 0)
  print(p)

my()

# ndfs의 방식과 dfs 방식의 결과는 같은데 이거도 가지치기로 봐야 하나? 동작 논리도 유사하다 dfs는 돌고나서 계산하고 ndfs는 돌기 전에 계산하고