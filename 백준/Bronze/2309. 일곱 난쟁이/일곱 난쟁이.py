import sys
from itertools import combinations

input = sys.stdin.readline
arr = []

for _ in range(9):
    dwf = int(input())
    arr.append(dwf)
arr.sort()

for x in combinations(arr, 7):
    if sum(x) == 100:
        for j in sorted(x):
            print(j)
        break
