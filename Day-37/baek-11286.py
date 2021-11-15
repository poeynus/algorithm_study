import heapq
import sys

input = sys.stdin.readline
h = []
heapq.heapify(h)

for i in range(int(input())):
    n = int(input())

    if n == 0:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
    else:
        heapq.heappush(h, (abs(n), n))

# 답은 맞는데 시간초과 나는 직접 짠 코드
# import sys

# input=sys.stdin.readline

# n = int(input())

# abs_heap = []

# for i in range(n):
#     x = int(input())

#     if x == 0:
#         if abs_heap:
#             print(abs_heap.pop(0))
#         else:
#             print(0)
#     else:
#         abs_heap.append(x)
#         abs_heap.sort()
#         abs_heap = sorted(abs_heap, key=abs)
