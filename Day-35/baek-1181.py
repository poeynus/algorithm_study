n = int(input())
w_list = []
for _ in range(n):
    w = input()
    w_cnt = len(w)
    w_list.append((w, w_cnt))
w_list = list(set(w_list))
w_list.sort(key= lambda word: (word[1], word[0]))

for i in w_list:
    print(i[0])