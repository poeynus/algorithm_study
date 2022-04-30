def DFS(v):
    if v>7:
        return
    else:  
        print(v, end=' ') # 전위
        DFS(v*2)
        print(v, end=' ') # 중위
        DFS(v*2+1)
        print(v, end=' ') # 후위
        
DFS(1)

# 처음부터 강의나 살 걸 뭐하러 이랬지 한번에 이해 되네