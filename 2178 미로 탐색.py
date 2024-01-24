'''
1278 미로 탐색
n×M크기의 배열로 표현되는 미로가 있다.
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (n, m)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
위의 예에서는 15칸을 지나야 (n, m)의 위치로 이동할 수 있다.
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

4 6
101111
101010
101011
111011

15
'''
from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0] # 위, 아래를 탐색한다.
dy = [0, 0, -1, 1] # 좌, 우를 탐색한다.
queue = deque()
queue.append((x, y))

# 너비 우선 탐색
def bfs(x, y):

    while queue:
        x, y = queue.popleft()  # 현재 x, y 위치를 queue에서 받는다.
    
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i] # 현재 위치에서 위, 아래를 확인한다.
            ny = y + dy[i] # 현재 위치에서 왼쪽, 오른쪽을 확인한다.

        # 네모칸을 벗어나는지 확인한다.
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
      
        # 벽이므로 진행 불가
        if graph[nx][ny] == 0:
            continue
      
        # 벽이 아니므로 이동
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            # 현재 위치의 값에 1을 더해 다음 위치에 1을 더한다.
            queue.append((nx, ny))
            # 다음 위치를 queue에 추가한다.
  
  # 마지막 값에서 카운트 값을 뽑는다.
    return graph[n-1][m-1]

print(bfs(0, 0))