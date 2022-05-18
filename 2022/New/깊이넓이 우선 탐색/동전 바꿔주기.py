cnt = 0
def my():
  n = int(input())
  m = int(input())
  coin = []
  coin_t = []

  for _ in range(m):
    c, t = map(int, input().split())
    coin.append(c)
    coin_t.append(t)

  # depth, sum
  def dfs(d, s):
    global cnt
    if s > n: # 가지 치기
      return
    if d == m:
      if s == n:
        cnt += 1
    else:
      for i in range(coin_t[d] + 1):
        dfs(d + 1, s + (coin[d] * i))

  dfs(0, 0)
  print(cnt)
my()

# 가지치기 했는데 한 번더 가능한가?