"""
실패
import sys
n = int(sys.stdin.readline())
tree = [0] * (n + 1)

for i in range(n-1):
    par, child, dist = map(int, sys.stdin.readline().strip().split())
    root = (par, child)
    tree[i] = {root : dist}

m = int(sys.stdin.readline())
for _ in range(m):
    a_par, a_child = map(int, sys.stdin.readline().strip().split())
    ans = (a_par, a_child)
    for i in tree:
        for key, value in i.items():
            if key == ans:
                print(value)
"""