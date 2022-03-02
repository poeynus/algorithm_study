tc = int(input())

stack = []

for i in range(tc):
    n = int(input())

    if n == 0:
        del stack[-1]
    else:
        stack.append(n)
print(sum(stack))