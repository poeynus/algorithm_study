def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for i in range(n):
        if visited[i] == False:
                dfs(n, computers, i, visited)
                answer += 1 
    print(answer)
    return answer

def dfs(n, computers, i, visited):
    visited[i] = True
    for connect in range(n):
        if connect != i and computers[i][connect] == 1: 
            if visited[connect] == False:
                dfs(n, computers, connect, visited)

solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])

# dfs bfs 플루이드 워셜