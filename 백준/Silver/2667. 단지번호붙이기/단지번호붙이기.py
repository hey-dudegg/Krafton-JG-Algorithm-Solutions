from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

cnt = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):

    queue = deque()
    graph[a][b] = 0
    queue.append((a, b))
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] != 1:
                continue
            else:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])