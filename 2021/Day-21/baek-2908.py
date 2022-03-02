a, b = map(str, input().split())
a = list(a)
b = list(b)
a = int(''.join(a[::-1]))
b = int(''.join(b[::-1]))
if(a > b):
    print(a)
else:
    print(b)