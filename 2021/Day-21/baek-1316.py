tc = int(input())
count = tc

for _ in range(tc):
    words = list(input())
    
    for i in range(len(words)-1):
        if(words[i] == words[i+1]):
            continue
        elif(words[i] in words[i+1:]):
            count -= 1
            break

print(count)    