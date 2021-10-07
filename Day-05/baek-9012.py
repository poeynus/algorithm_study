
tc = int(input())

for _ in range(tc):
    input_list = list(input())
    stack = []
    check = True
    for i in input_list:
        if  i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                check = False
    if stack or check == False:
        print("NO")
    else:
        print("YES")
        