from collections import deque

def my():
  n, k = map(int, input().split())
  n = [x for x in range(1, n+1)]
  d = deque(n)
  cnt = 1

  while len(d) > 1:
    if cnt < k:
      d.append(d.popleft())
    elif cnt == k:
      d.popleft()
    else:
      cnt = 0
    cnt += 1

  print(''.join(map(str, list(d))))

def solution():
  n, k=map(int, input().split())
  q=list(range(1, n+1))
  dq=deque(q)
  while dq:
      for _ in range(k-1):
          cur=dq.popleft()
          dq.append(cur)
      dq.popleft()
      if len(dq)==1:
          print(dq[0])
          dq.popleft()
  

my()

# n k 입력 받고
# k 횟수 만큼 popleft 후 append 진행 
# k 횟수에 도달하면 popleft만 진행 반복 횟수는 길이가 1이 될 때 까지

# 쉽게 풀었슴다