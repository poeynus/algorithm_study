mi = 2147000000
def my():
  n = int(input())
  coin = list(int(input()) for _ in range(n))

  # depth, Asum, Bsum, Csum
  def dfs(d, asum, bsum, csum):
    global mi
    if d == n:
      cha = max(asum, bsum, csum) - min(asum, bsum, csum)
      if mi > cha > 0 and asum != bsum and asum != csum and bsum != csum:
        mi = cha
    else:
      dfs(d + 1, asum + coin[d], bsum, csum)
      dfs(d + 1, asum, bsum + coin[d], csum)
      dfs(d + 1, asum, bsum, csum + coin[d])
  
  dfs(0, 0, 0, 0)
  print(mi)
my()

# 일단 다 구하고 최소차 갱신 하는 방식으로 가자, 매개 변수 4개로 하면 편할듯?
# 아 문제를 제대로 안읽고 세사람 동일한 걸로 풀어서 한참 걸렸네 문제를 제대로 읽자.

# 요즘에 좀 어지럽네 병원을 가야 하나