word = input().lower()

w_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

result = []

for i in w_list:
    c = word.count(i)
    result.append(c)

if result.count(max(result)) > 1:
    print("?")
else:
    print(w_list[result.index(max(result))].upper())