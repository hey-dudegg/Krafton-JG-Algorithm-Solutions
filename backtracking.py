import sys
input = sys.stdin.readline

a = []
n, m = map(int, input().split())

def btrk():
    if len(a) == m:
        print(" ".join(map(str, a)))
        return
    
    for i in range(1, n + 1):
        if i not in a:
            a.append(i)
            btrk()
            a.pop()

btrk()