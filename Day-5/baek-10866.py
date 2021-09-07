import sys

input = sys.stdin.readline

deque = []

tc = int(input())

for _ in range(tc):
    msg = list(map(str, input().split()))

    if msg[0] == "push_front":
        deque.insert(0, int(msg[1]))
    elif msg[0] == "push_back":
        deque.append(int(msg[1]))
    elif msg[0] == "pop_front":
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif msg[0] == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)       
    elif msg[0] == "size":
        print(len(deque))
    elif msg[0] == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif msg[0] == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif msg[0] == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)