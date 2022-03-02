word = list(input())

for i in range(len(word)):
    word[i] = int(ord(word[i]))-3
    if(word[i] == 62):
         word[i] = 88
    elif(word[i] == 63):
        word[i] = 89
    elif(word[i] == 64):
        word[i] = 90
    print(chr(word[i]), end="")