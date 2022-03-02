num = int(input())

for i in range(num):
    for _ in range(i+1):
        print("*", end="")
    print("")
