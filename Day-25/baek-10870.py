
def fivo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fivo(n-1) + fivo(n-2)

t = int(input())

print(fivo(t))

    