""" EOF error 코드.
a = []

def sum(n):
    if n < 1000001:
        sum = 0
        i = 0
        for i in range(n+1): # n+1까지 더해줘야 n까지 더해짐
            a.append(i)
            sum += int(a[i])
        return sum
    else:
        return

n = int(input())
print(sum(n))
"""

def solve(a: list) -> int:
    return sum(a)
