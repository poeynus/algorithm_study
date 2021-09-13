from collections import deque

def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

v, e, s = map(int, input().split())

stack = [[] for _ in range(v+1)]
dfs_visited = [False for _ in range(v+1)]
bfs_visited = [False for _ in range(v+1)]

for i in range(e):
    fi, se = map(int, input().split())
    stack[fi].append(se)
    stack[se].append(fi)
    
for i in stack:
    i.sort()

dfs(stack, s, dfs_visited)
print()
bfs(stack, s, bfs_visited)