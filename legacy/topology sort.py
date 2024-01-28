from collections import deque

v, e = 7, 8  # 원하는 값으로 수정

indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

edges = [
    (1, 2),
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 4),
    (4, 7),
    (5, 6),
    (6, 4),
]

for edge in edges:
    a, b = edge
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for g in graph[now]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)

    for res in result:
        print(res, end=' ')

topology_sort()



"""

import sys
from collections import deque


v, e = map(int, sys.stdin.readline().split())

# 노드의 개수와 간선의 개수
indegree = [0] * (v + 1)
# 모든 노드에 대한 진입차수는 0으로 초기화
graph = [[] for _ in range(v + 1)]
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트

for _ in range(e):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for g in grapth[now]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)

    # 위상 정렬 수행한 결과 출력
    for res in result:
        print(res, end = ' ')

topology_sort()

"""