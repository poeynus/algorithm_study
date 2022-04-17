def my():
  n = int(input())
  madang = [list(map(int, input().split())) for _ in range(n)]
  m =  int(input())
  d = 0
  e = n
  result = 0

  for _ in range(m):
    a, b, c = map(int, input().split())
    for _ in range(c):
      if b == 0:
        madang[a-1].append(madang[a-1].pop(0))
      else:
        madang[a-1].insert(0, madang[a-1].pop())

  for i in range(n):
    for j in range(d, e):
      result += madang[i][j]

    if i >= n // 2:
      d -= 1
      e += 1
    else:
      d += 1
      e -= 1

  print(result)

def solution():
  n = int(input())
  a = [list(map(int, input().split())) for _ in range(n)]
  m =  int(input())
  for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
      for _ in range(k):
        a[h-1].append(a[h-1].pop(0))
    else:
      for _ in range(k):
        a[h-1].insert(0, a[h-1].pop())
  res = 0
  s= 0
  e=n-1
  for i in range(n):
    for j in range(s, e+1):
      res+=a[i][j]
    if i<n//2:
      s+=1
      e-=1
    else:
      s-=1
      e+=1
  print(res)
my()

# 첫 줄은 n 홀수 둘째 줄 부터 자연수
# 셋째 줄 m 넷째 줄 회전 명령
# 이번에도 강사님이랑 비슷하게 풀이