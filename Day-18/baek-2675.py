tc = int(input())

for _ in range(tc):
    n, word = map(str, input().split())

    word_list = list(word)


    for i in range(len(word_list)):
        for _ in range(int(n)):
            print(word_list[i], end="")
    print()