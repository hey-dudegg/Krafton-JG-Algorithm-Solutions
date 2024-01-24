'''
1260 DFS와 BFS

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.

입력 : 
4 5 1
1 2
1 3
1 4
2 4
3 4

출력 :
1 2 4 3
1 2 3 4
'''
from collections import deque
import sys

input = sys.stdin.readline
n, m, v = map(int, input().split())
elist = [[] for _ in range(m + 1)]
stack = deque()
stack.append(v)
visited = [0] * (n + 1)

for i in range(m+1):
    s, e = map(int, input().split())
    elist[s].append(e)
    elist[e].append(s)

for i in range(1,6):
    for j in range(len(elist[i])- 1):
        if elist[i][j] > elist[i][j+1]:
            elist[i][j], elist[i][j+1] = elist[i][j+1], elist[i][j]

while stack:
    now = stack.pop() #
    if visited[now] == 0:
        visited[now] = 1
        print(now, end = " ")
        for x in elist[now][::-1]:
            stack.append(x)

print("")
stack = deque()
stack.append(v)

visited = [0] * (n + 1)

while stack:
    now = stack.popleft()
    if visited[now] == 0:
        visited[now] = 1
        print(now, end = " ")
        for x in elist[now]:
            stack.append(x)
