import sys
import time
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    a, b, c = 1, 2, 4
    for _ in range(1, n):
        a, b, c = b, c, a + b + c
    print(a)