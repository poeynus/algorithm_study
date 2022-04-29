import heapq

def my():
  heap = []

  while True:
    n = int(input())

    if n == -1:
      break
    elif n == 0:
      if len(heap) == 0:
        print('-1')
      else:
        print(heapq.heappop(heap))
    else:
      heapq.heappush(heap, n)

def solution():
  # 모듈을 쓰는 거라 똑같음
  pass

my()

# 힙을 한번 직접 만들어 볼까 개같이 포기