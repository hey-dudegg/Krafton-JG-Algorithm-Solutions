'''
2665 미로 만들기
n×n 바둑판 모양으로 총 n2개의 방이 있다. 일부분은 검은 방이고 나머지는 모두 흰 방이다. 

검은 방은 사면이 벽으로 싸여 있어 들어갈 수 없다. 서로 붙어 있는 두 개의 흰 방 사이에는 문이 있어서 지나다닐 수 있다.
윗줄 맨 왼쪽 방은 시작방으로서 항상 흰 방이고, 아랫줄 맨 오른쪽 방은 끝방으로서 역시 흰 방이다.
시작방에서 출발하여 길을 찾아서 끝방으로 가는 것이 목적인데, 아래 그림의 경우에는 시작방에서 끝 방으로 갈 수가 없다.
부득이 검은 방 몇 개를 흰 방으로 바꾸어야 하는데 되도록 적은 수의 방의 색을 바꾸고 싶다.

아래 그림은 n=8인 경우의 한 예이다.
위 그림에서는 두 개의 검은 방(예를 들어 (4,4)의 방과 (7,8)의 방)을 흰 방으로 바꾸면,
시작방에서 끝방으로 갈 수 있지만, 어느 검은 방 하나만을 흰 방으로 바꾸어서는 불가능하다.
검은 방에서 흰 방으로 바꾸어야 할 최소의 수를 구하는 프로그램을 작성하시오.

단, 검은 방을 하나도 흰방으로 바꾸지 않아도 되는 경우는 0이 답이다.

8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111

2
'''
'''
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
maze = []

for _ in range(n):
    maze.append(list(map(int, input())))

print(maze)
mx = [1, 0]
my = [0, 1]
q = deque()
q.append((0,0))
min = [0]

def bfs():
    while q:
        for _ in range(n):
            w = 0
            x, y = q.popleft()
            
            for i in range(2):
                nx = x + mx[i]
                ny = y + my[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if maze[nx][ny] == 0:
                    q.append((nx, ny))
                    w += 1
                    if w > int(min[0]):
                        min[0] = w

                else:
                    q.append((nx,ny))

    return print(int(min[0]))

bfs()
'''

# 미로만들기
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
arr = []

for i in range(N):
    arr.append(list(map(int, input().strip())))

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        if x == N-1 and y == N-1:
            return visited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if arr[nx][ny] == 1:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

print(bfs())