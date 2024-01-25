import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# print(graph)

dx = [1, -1, 0, 0]
dy = [0, 0 , 1, -1]

visited = set()
que = deque()
danji = set()
count = 0

def bfs(que,visited):

    path = 0
    while que:

        path += 1
        x, y = que.popleft()
        visited.add((x,y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx <= n-1 and 0<=ny <=n-1:
                if graph[nx][ny] == 1 and (nx, ny) not in visited:
                    que.append((nx,ny))
                    visited.add((nx,ny))
                    graph[nx][ny] = path


for i in range(n):
    for j in range(n):
        if (i, j) not in visited and graph[i][j] == 1:
            count +=1
            que.append((i,j))
            bfs(graph,que,visited)

## 해당하는 단지마다의 path를 출력해야하는데, 
# 이 코드는 단지의 path가 동일하면 한번 출력됨..
# 마지막 단지의 번호를 저장해서 그 집의 총 갯수와 그 집의 Path로 요소 갯수 내면??
for i in range(n):
    for j in range(n):
        if graph[i][j] not in danji:
            danji.add(graph[i][j])

danji_list = list(danji)

danji_list.sort()

# print(danji_list)

danji_list_reversed = danji_list[::-1][:count]

print(count)
# print(danji_list_reversed)

danji_list_reversed.sort()


#그리고 path(단지 요소 갯수)가 1정도 차이가 나는데 왜인지 모르겠군..<

for i in danji_list_reversed:
    print(i+1)
