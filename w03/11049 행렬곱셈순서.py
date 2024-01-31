'''
11049 햅렬 곱셈 순서
크기가 N×M인 행렬 A와 M×K인 B를 곱할 때 필요한 곱셈 연산의 수는 총 N×M×K번이다.
행렬 N개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.
예를 들어, A의 크기가 5×3이고, B의 크기가 3×2, C의 크기가 2×6인 경우에 행렬의 곱 ABC를 구하는 경우를 생각해보자.

AB를 먼저 곱하고 C를 곱하는 경우 (AB)C에 필요한 곱셈 연산의 수는 5×3×2 + 5×2×6 = 30 + 60 = 90번이다.
BC를 먼저 곱하고 A를 곱하는 경우 A(BC)에 필요한 곱셈 연산의 수는 3×2×6 + 5×3×6 = 36 + 90 = 126번이다.
같은 곱셈이지만, 곱셈을 하는 순서에 따라서 곱셈 연산의 수가 달라진다.

행렬 N개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성하시오.
입력으로 주어진 행렬의 순서를 바꾸면 안 된다.

입력
3
5 3
3 2
2 6

출력
90
'''
import sys
input = sys.stdin.readline

def main():
    for c in range(1, N):   # c: 행렬 개수
        for s in range(N-c):    # s: 시작 인덱스
            t0, e = INF, s+c    # t0: s~e 번째 행렬의 곱셈 연산 수 초기값, e: 마지막 인덱스
            i, j = dp[s][s:e], dp[e][s+1:e+1]
            k, ns = num[s]*num[e+1], num[s+1:e+1]
            for m in range(e-s):   # m: 중간 인덱스
                if t0 > (t:=i[m] + k*ns[m] + j[m]):
                    t0 = t
            dp[s][e] = dp[e][s] = t0
    print(dp[0][N-1])


INF = 2**31
N = int(input())
f = lambda: tuple(map(int, input().split()))
num = [*f()] + [f()[1] for _ in range(N-1)]
dp = [[0]*N for _ in range(N)]
main()