num_list = []
max_num = 0
for i in range(7):
    imsi = int(input())
    if imsi & 1:
        num_list.append(imsi)
        max_num+=imsi
if(max_num == 0):
    print(-1)
else:
    print(max_num)
    print(min(num_list))
