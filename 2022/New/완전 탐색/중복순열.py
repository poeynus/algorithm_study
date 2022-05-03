chk = []
cnt = 0

def my():
  global chk
  global cnt
  n, m = map(int, input().split())
  chk = [0] * m

  dfs(0, m, n)
  print(cnt)

# x = 숫자, f = 최대 크기, a = 숫자
def dfs(x, f, a):
  global chk
  global cnt
  if x == f:
    cnt += 1
    print(' '.join(map(str, chk)))
    return
  else:
    for i in range(1, a + 1):
      chk[x] = i
      dfs(x + 1, f, a)
my()

# 지금까지는 이진트리 형태로 간단하게 할 수 있었는데 이제는 트리가 여러가닥이다