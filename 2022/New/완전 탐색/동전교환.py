res = 2147000000

def my():
  global res
  n = int(input())
  n_list = list(map(int, input().split()))
  m = int(input())
  n_list.sort(reverse=True)
  dfs(0, n_list, m, 0)
  print(res)

# x = 코인 수, li = 분할 목록, w = 분할 목표, s = 더한 값
def dfs(x, li, w, s):
  global res
  if res < x:
    return
  if s == w and x < res:
    res = x
  elif s > w:
    return
  else:
    for i in li:
      dfs(x + 1, li, w, s+i)


my()

# 될 듯 하다가도 안된다잉.