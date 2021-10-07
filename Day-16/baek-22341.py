n, tc = map(int, input().split())

r_x = n
r_y = n

for i in range(tc):
    x, y = map(int, input().split())

    if x >= n or y >= n or x == 0 or y == 0:
        continue

    if x * r_y >= r_x * y:
        r_x = x
    
    else:
        r_y = y

print(r_x * r_y)