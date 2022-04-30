from collections import deque

def my():
  n, m = map(int,input().split())
  h = list(map(int, input().split()))
  h = list(enumerate(h))
  d = deque(h)
  cnt = 0

  # while True:
  #   print(d, cnt)
  #   if any(d[1] < x[1] for x in d):
  #     if d[0][0] == m:
  #       cnt += 1
  #       break
  #     else:
  #       cnt += 1
  #       d.popleft()
  #   else:
  #     d.append(d.popleft())

  print(cnt)

def solution():
  n, m=map(int, input().split())
  Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
  Q=deque(Q)
  cnt=0
  while True:
      cur=Q.popleft()
      if any(cur[1]<x[1] for x in Q):
          Q.append(cur)
      else:
          cnt+=1
          if cur[0]==m:
              print(cnt)
              break

my()

# popleft 꺼내고 이거보다 위험도 높은 환자 있으면 제일 뒤로 아니면 바로 진료, 같은 값도 진료
# 이 문제를 못 풀었는데 내가 범위를 못잡아서 못풀었다. any함수 안에 조건 법을 공부해야 할 듯