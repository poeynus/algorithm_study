
case = int(input())

connect = int(input())

count = []

def dfs(graph, v, visited, c):
    visited[v]=True
    c.append(1)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, c)

d_list = [[] for _ in range(case+1)]
d_visited = [False for _ in range(case+1)]

for i in range(connect):
    a, b = map(int, input().split())
    d_list[a].append(b)
    d_list[b].append(a)

dfs(d_list, 1, d_visited, count)
print(len(count)-1)