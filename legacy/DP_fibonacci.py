'''
import sys
import time

input = sys.stdin.readline
n = int(input())
start = time.time()

def recursion_fibo(n):
    return 1 if n<=2 else recursion_fibo(n-2) + recursion_fibo(n-1)

print(f"n이 {n}일 때 :")
print(f"Fibo_Recur : {recursion_fibo(n)}, Time : {time.time() - start:.16f}sec")
'''
'''
import time
import sys

n = int(sys.stdin.readline())
start = time.time()

def dp_fibo(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]

print(f"n이 {n}일 때 :")
print(f"Fibo_DP Result: {dp_fibo(n)}, Time: {time.time() - start:.16f} sec")
'''
'''
import sys
import time

input = sys.stdin.readline
n = int(input())

start = time.time()

a, b = 0, 1
for i in range(n):
    a, b = b, a + b

print(f"n이 {n}일 때 :")
print(f"Fibo_Loop Result: {a}, Time: {time.time() - start:.16f} sec")

# n = 30 > Plus with loop : (832040, 1346269), Time : 0.0000000000000000sec
# n = 10000 > Time : 0.0029883384704590sec
'''