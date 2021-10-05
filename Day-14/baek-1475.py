# import math

# d_n = list(map(int, input()))

# d_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# for i in d_n:
#     if i == 0:
#         d_list[0] = d_list[0] + 1 
#     elif i == 1:
#         d_list[1] = d_list[1] + 1
#     elif i == 2:
#         d_list[2] = d_list[2] + 1
#     elif i == 3:
#         d_list[3] = d_list[3] + 1
#     elif i == 4:
#         d_list[4] = d_list[4] + 1
#     elif i == 5:
#         d_list[5] = d_list[5] + 1
#     elif i == 6 or i == 9:
#         d_list[6] = d_list[6] + 1
#     elif i == 7:
#         d_list[7] = d_list[7] + 1
#     elif i == 8:
#         d_list[8] = d_list[8] + 1

# d_list[6] = math.ceil(d_list[6]/2)

# print(max(d_list))


d_n = list(map(int, input()))
d_list = []

for i in range(10):
    d_list.append(d_n.count(i))

d_list[6] = (d_list[6] + d_list[9] + 1)//2
    
del d_list[9]

print(max(d_list))