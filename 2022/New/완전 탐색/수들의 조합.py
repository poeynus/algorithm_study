cnt = 0

def my():
  n, k = map(int, input().split())
  li = list(map(int, input().split()))
  x = int(input())
  
  p = [0] * k # 조합 담을 배열

  # d = p의 depth, id = li의 depth 
  def dfs(d, id):
    global cnt
    if d == k and sum(p) % x == 0:
      cnt += 1
    elif d == k and sum(p) % x != 0:
      return
    else:
      for i in range(id, n):
        p[d] = li[i]
        dfs(d + 1, i + 1)

  dfs(0, 0)
  print(cnt)

my()

# 좋습니다