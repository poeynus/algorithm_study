n_list = [x for x in range(1, 10001)]
result = [x for x in range(1, 10001)]

for i in n_list:
    a = list(str(i))
    a = [int(i) for i in a]
    n = sum(a) + i
    
    if n in result:
        result.remove(n)
for i in result:
    print(i) 
    