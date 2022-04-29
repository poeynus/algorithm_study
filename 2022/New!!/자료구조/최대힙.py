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
        print(-heapq.heappop(heap))
    else:
      heapq.heappush(heap, -n)

def solution():
  pass

my()

# 이거는 잘 몰라서 그대로 봄
# 최대 힙은 입력 할 때 정수를 -로 바꿔서 입력하면 간단하게 응용 가능 나중에 꺼낼때는 다시 -제거