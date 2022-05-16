p = 0
def my():
  n, m = map(int, input().split())
  s_list= []
  t_list = []

  for _ in range(n):
    s, t = map(int, input().split())
    s_list.append(s)
    t_list.append(t)

  def dfs(d, all, time, cut):
    global p
    if time > m:  # 가지치기 한 번
      return
    if all + sum(s_list) - cut < p: # 가지치기 두 번
      return
    if d == n:
      if all > p:
        p = all
    else:
      dfs(d+1, all + s_list[d], time + t_list[d], cut + s_list[d])
      dfs(d+1, all, time, cut + s_list[d])

  dfs(0, 0, 0, 0)
  print(p)

my()

# 가지치기는 성능이 확실히 좋아진다.
# 계산의 경우의 갈래가 여러가지가 아닌 O, X의 경우에는 반복문 말고 dfs를 두 번 돌리자