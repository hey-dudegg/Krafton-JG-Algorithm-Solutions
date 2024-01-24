import sys

n = int(sys.stdin.readline())
list = [x + 1 for x in range(n)]
used = [0] * n

def perm(arr, n):
    if n == len(list):
        print(" ".join(map(str, arr)))
        return
    
    for i in range(len(list)):
        if not used[i]:
            used[i] = 1
            arr.append(list[i])
            perm(arr, n+1)
            arr.pop()
            used[i] = 0

perm([], 0)