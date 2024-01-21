import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

graph = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
visited[1] = 1

def dfs(now):
    for nxt in graph[now]:
        if visited[nxt] == 0:
            visited[nxt] = now
            dfs(nxt)

dfs(1)

for x in range(2 , n + 1):
    print(visited[x])