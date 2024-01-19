import sys
n = int(sys.stdin.readline())
tree = [] * n

for i in range(n):
    par, child, dist = map(int, sys.stdin.readline().strip().split())
    if par > child:
        par, child = child, par

    root = (par, child)
    tree[i] = {root : dist}

print(tree)