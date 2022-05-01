a = 0 # 집합으로 사용
b = 0 # 집합으로 안사용
flag = False

def my():
  global a
  global b
  global flag
  n = int(input())
  arr = list(map(int, input().split()))
  chk = [0] * n

  dfs(0, arr, chk)
  
  if flag:
    print('YES')
  else:
    print('NO')
  

def dfs(x, ary, ch):
  global a
  global b
  global flag
  if x == len(ary):
    for i in range(x):
      if ch[i] == 1:
        a += ary[i]
      else:
        b += ary[i]
    if a == b:
      flag = True
      return
    else:
      a = 0
      b = 0
  else:
    ch[x] = 1
    dfs(x + 1, ary, ch)
    ch[x] = 0
    dfs(x + 1, ary, ch)

my()

# 내가 직접 짰수다