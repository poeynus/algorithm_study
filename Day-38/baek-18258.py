import sys 
input = sys.stdin.readline 
n = int(input()) 
queue = [] 
cnt = 0 
for i in range(n): 
    msg = input().strip() 
    if msg.split()[0] =='push': 
        queue.append(int(msg.split()[1])) 
    elif msg.split()[0]=='pop': 
        if len(queue)-cnt ==0: print(-1) 
        else: 
            print(queue[cnt]) 
            cnt += 1 
    elif msg.split()[0]=='size': 
        print(len(queue)-cnt) 
    elif msg.split()[0] =='empty': 
        if len(queue)-cnt ==0: 
            print(1)
        else: 
            print(0) 
    elif msg.split()[0]=='front': 
        if len(queue)-cnt ==0: print(-1) 
        else: 
            print(queue[cnt]) 
    elif msg.split()[0]=='back': 
        if len(queue)-cnt==0: 
            print(-1) 
        else: 
            print(queue[-1])
