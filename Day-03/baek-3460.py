tc = int(input())

for _ in range(tc):
    imsi = int(input())
    imsi = bin(imsi)[::-1]

    for i in range(len(imsi)):
        if imsi[i] == "1":
            print(i, end=" ")
    print("")