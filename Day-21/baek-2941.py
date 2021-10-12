word = input()

w_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = 0
a = 0

while(a != len(w_list)):
    count += word.count(w_list[a])
    word = word.replace(w_list[a], " ")
    a += 1    

print(count)