tc = int(input())

a_li = []

for _ in range(tc):
    n = int(input())
    a_li.append(n)

a_li = sorted(a_li)

for i in a_li:
    print(i)