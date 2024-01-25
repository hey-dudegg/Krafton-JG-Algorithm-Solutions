import sys

input = sys.stdin.readline
n, m = map(int, input().split())
d = [-1, 1]
g = []
for _ in range(n):
    g.append(list(input()))

def dfs(x, y):

    if g[x][y] == '-':
        g[x][y] = 1	

        for i in d:  
            ny = y + i

            if 0 < ny < m and g[x][ny] == '-':
                dfs(x, ny)

    if g[x][y] == '|':
        g[x][y] = 1

        for i in d:   
            nx = x +  i 

            if (nx > 0 and nx < n) and g[nx][y] == '|':
                dfs(nx, y)

cnt = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == '-' or g[i][j] == '|':
            dfs(i, j)
            cnt += 1

print(cnt)
