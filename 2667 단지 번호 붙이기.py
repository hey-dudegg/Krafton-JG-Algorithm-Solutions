'''
2667 단지번호 붙이기

<그림 1>과 같이 정사각형 모양의 지도가 있다.
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

입력
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

출력
3
7
8
9

'''
'''
n = int(input())
graph = []
count = []
cnt = [0]

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        cnt[0] += 1
        graph[x][y] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            DFS(nx, ny)
        return True
    return False

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            count.append(cnt[0])
            cnt[0] = 0

count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])

'''

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
