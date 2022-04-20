def my():
  pass

def solution():
  n, c = map(int, input().split())
  Line = []
  for _ in range(n):
    tmp = int(input())
    Line.append(tmp)
  Line.sort()
  lt=1
  rt=Line[n-1]
  while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid, Line)>=c:
      res=mid
      lt=mid+1
    else:
      rt=mid-1
  print(res)

def Count(len, Line):
  cnt = 1
  ep=Line[0]
  for i in range(1, n):
    if Line[i]-ep>=len:
      cnt+=1
      ep=Line[i]
  return cnt
  
# 허허 이번엔 손도 못대었네;;