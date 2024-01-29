N = int(input())
mat = []

for _ in range(N):
    r, c = map(int, input().split())
    mat.append((r, c))

dp = [[0]*N for _ in range(N)] 

for i in range(N-1):
    dp[i][i+1] = mat[i][0]*mat[i+1][0]*mat[i+1][1]
    
for L in range(2, N):
    i = 0    
    j = L    
    
    while j < N:
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] +
                           mat[i][0]*mat[k][1]*mat[j][1])
        i += 1
        j += 1 

print(dp[0][N-1])