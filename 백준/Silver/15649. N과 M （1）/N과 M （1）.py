import sys
input = sys.stdin.readline

def back_trk():
    if m == len(a):
        print(" ".join(map(str, a)))
        return
    
    for i in range(1, n + 1):
        if i not in a:
            a.append(i)
            back_trk()
            a.pop()

a = []
n, m = map(int, input().split())

back_trk()