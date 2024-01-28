'''
9084 동전
우리나라 화폐단위, 특히 동전에는 1원, 5원, 10원, 50원, 100원, 500원이 있다.
이 동전들로는 정수의 금액을 만들 수 있으며 그 방법도 여러 가지가 있을 수 있다.
예를 들어, 30원을 만들기 위해서는 1원짜리 30개 또는 10원짜리 2개와 5원짜리 2개 등의 방법이 가능하다.
동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법을 세는 프로그램을 작성하시오.

입력

3
2
1 2
1000
3
1 5 10
100
2
5 7
22

출력
501
121
1
'''


import sys

input = sys.stdin.readline
t = int(input()) # 전체 테스트 케이스 개수

for _ in range(t):
    n = int(input()) # 해당 케이스의 코인 갯수
    coins = list(map(int, input().strip().split())) # 코인의 종류
    cost = int(input().rstrip()) # 코인으로 만들어야 할 총 비용
    DP = [0] * (cost + 1) 
    # 비용을 0부터 cost까지 코인의 종류 따른 경우의 수를 저장할 DP 리스트 생성
    DP[0] = 1 # 동전의 종류와 상관없이 0원을 만들 경우의 수는 1
    
    for coin in coins: # 코인의 종류에 따라 DP를 갱신하기 위해 코인을 꺼냄
        for i in range(1, cost + 1):
            if coin > i: # i가 coin보다 클 때는 경우의 수가 갱신되지 않는다.
                continue
            else:
                DP[i] = DP[i - coin] + DP[i] # ex) DP[4] = DP[4 - coin] + DP[4]
    print(DP[cost]) # 반복문이 끝난 후 총비용을 만들 경우의 수 출력
'''

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    coins.insert(0, 0)
    M = int(sys.stdin.readline())

    dp = [[0] * (M+1) for i in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1

    for j in range(1, N+1):
        for i in range(1, M+1):
            dp[j][i] = dp[j-1][i]
            if i-coins[j] >= 0:
                dp[j][i] += dp[j][i-coins[j]]
    print(dp[N][M])
'''