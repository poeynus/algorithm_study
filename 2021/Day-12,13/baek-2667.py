line = int(input())

graph = [list(map(int, input())) for _ in range(line)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

count = 0
num = 0
result = []

def DFS(x, y):
    if x < 0 or x >= line or y < 0 or y>= line:
        return False
    
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True

for i in range(line):
    for j in range(line):
        if DFS(i,j) == True:
            num += 1
            result.append(count)
            count = 0
result.sort()
print(num)
for i in result:
    print(i)