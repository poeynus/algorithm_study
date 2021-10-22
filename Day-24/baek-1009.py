
tc = int(input())

for _ in range(tc):
    a, b = map(int, input().split())

    c = pow(a,b,10)
    
    if c:
        print(c)
    else:
        print(10) 
