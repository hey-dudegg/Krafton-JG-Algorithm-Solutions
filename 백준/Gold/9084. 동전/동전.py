import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().strip().split()))
    cost = int(input().rstrip())
    DP = [0] * (cost + 1)
    DP[0] = 1 # 
    
    for coin in coins:
        for i in range(1, cost + 1):
            if coin > i:
                continue
            else:
                DP[i] = DP[i - coin] + DP[i]
    print(DP[cost])