import sys

input = sys.stdin.readline

queue = []

tc = int(input())

for _ in range(tc):
    msg = list(map(str, input().split()))

    if msg[0] == "push":
        queue.append(int(msg[1]))
    elif msg[0] == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif msg[0] == "size":
        print(len(queue))
    elif msg[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif msg[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif msg[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)