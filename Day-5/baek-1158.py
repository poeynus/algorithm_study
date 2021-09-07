n, k = map(int, input().split())

n_list = [x for x in range(1, n+1)]

result = []

count = k-1

while len(n_list):
    if count >= len(n_list):
        count = count % len(n_list)
    else:
        result.append(str(n_list.pop(count)))
        count += k-1
 
print("<", ", ".join(result), ">", sep='')