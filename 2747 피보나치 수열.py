"""
# 재귀 함수로 구현
n = int(input())

def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)


print(Fibonacci(n))
"""

n = int(input())

a, b = 0, 1
for i in range(n):
    a, b = b, a+b

print(a)