'''
11047 동전 0
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

출력
6
'''
# 동전을 리스트에 요소들로 저장하고 내림차순으로 정렬한다.
# for문으로 


import sys
input = sys.stdin.readline

n, cost = map(int, input().strip().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse = True)
cnt = [0]

for coin in coins:
    if cost >= coin:
        a = cost // coin
        if a > 0:
            cost -= a * coin
            cnt[0] += a

print(cnt[0])
'''

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
'''