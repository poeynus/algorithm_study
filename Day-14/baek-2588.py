a = list(map(int, input()))
b = list(map(int, input()))

f = (a[0] * 100 * b[2]) + (a[1] * 10 * b[2]) + (a[2] * b[2])
s = (a[0] * 100 * b[1] * 10) + (a[1] * 10 * b[1] * 10) + (a[2] * b[1] * 10)
t = (a[0] * 100 * b[0] * 100) + (a[1] * 10 * b[0] * 100) + (a[2] * b[0] * 100)
result = f + s + t

print(f)
print(int(s/10))
print(int(t/100))
print(result)
