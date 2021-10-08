n, tc = map(int, input().split())

r_x = n
r_y = n

for i in range(tc):
    x, y = map(int, input().split())

    if x >= r_x or y >= r_y:
        continue

    elif x * r_y >= r_x * y:
        r_x = x
    
    else:
        r_y = y

print(r_x * r_y)