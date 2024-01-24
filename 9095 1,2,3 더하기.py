'''
import time
import sys

n = int(sys.stdin.readline())
start = time.time()

dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 4
    else:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

print(f"n이 {n}일 때 :")
print(f"Plus with Dynamic Programming : {dp[n]}, Time : {time.time() - start:.16f}sec")
'''
'''
import sys
import time

n = int(sys.stdin.readline())
start = time.time()

def recur(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return recur(n - 1) + recur(n - 2) + recur(n - 3)
    
print(f"n이 {n}일 때 :")
print(f" Plus with Recursion : {recur(n)}, Time : {time.time() - start:.16f}sec")
# recur(30) : Plus with Recursion : 53798080, Time : 55.1620876789093018sec
'''
'''

import sys
import time

n = int(sys.stdin.readline())
start = time.time()
a, b, c = 1, 2, 4

for _ in range(1, n):
    a, b, c = b, c, a + b + c

print(f"n이 {n}일 때 :")
print(f"Plus with loop: {a}, Time: {time.time() - start:.16f} sec")
'''
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