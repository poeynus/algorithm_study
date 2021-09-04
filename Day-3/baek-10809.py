word_list = {"a": -1, "b": -1, "c": -1, "d": -1, "e": -1, "f": -1, "g": -1, "h": -1, "i": -1, "j": -1, "k": -1, "l": -1, "m": -1, "n": -1, "o": -1, "p": -1, "q": -1, "r": -1, "s": -1, "t": -1, "u": -1, "v": -1, "w": -1, "x": -1, "y": -1, "z": -1}

word = input()

for i in range(len(word)):
    if word_list[word[i]] == -1:
        word_list[word[i]] = i
        
for i in word_list.values():
    print(i, end=" ")