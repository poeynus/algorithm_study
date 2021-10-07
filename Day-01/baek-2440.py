num = int(input())

for i in range(num):
    for _ in range(num-i):
        print("*", end="")
    print("")