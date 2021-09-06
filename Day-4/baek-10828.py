import sys

input = sys.stdin.readline  # 이런거 있을 줄은 몰랐네

stack = []

tc = int(input())

for _ in range(tc):
    msg = list(map(str,input().split()))
    
    if msg[0] == "push":
        stack.append(int(msg[1]))
    elif msg[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif msg[0] == "size":
        print(len(stack))
    elif msg[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif msg[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)