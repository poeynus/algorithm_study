tc = int(input())

for _ in range(tc):
    result = 0
    count = 0
    a = []
    
    word = list(input())
    
    for i in word:
        if i == 'O':
            count += 1
        else:
            a.append(count)
            count = 0
    a.append(count)
    count = 0

    for i in range(len(a)):
        result += int(a[i] * (a[i]+1) / 2)

    print(result)