'''
9251 LCS
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
ACAYKP
CAPCAK

출력
4
'''
'''
# LCS(Longest Common Subsequence)
import sys
input = sys.stdin.readline

A = " " + input().strip()
B = " " + input().strip()
LCS = [[0 for _ in range(len(B))] for _ in range(len(A))]
cnt = 0

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
            if LCS[i][j] > cnt:
                cnt = LCS[i][j]
        else:
            LCS[i][j] = max(LCS[i][j - 1], LCS[i - 1][j])

print(cnt)
'''
# LCS(Longest Common Substring)
import sys

input = sys.stdin.readline
A = " " + input().strip()
B = " " + input().strip()
cnt = 0
LCS = [[0 for _ in range(len(B))] for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
            if LCS[i][j] > cnt:
                cnt = LCS[i][j]
        else:
            LCS[i][j] = 0

print(cnt)
