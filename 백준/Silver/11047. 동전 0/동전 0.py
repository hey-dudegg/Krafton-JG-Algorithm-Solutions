import sys
input = sys.stdin.readline

n, cost = map(int, input().strip().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse = True)
cnt = [0]

for coin in coins:
    cnt[0] += cost // coin
    cost = cost % coin
        
print(cnt[0])