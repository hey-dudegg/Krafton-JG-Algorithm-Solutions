Case = int(input())

for i in range(Case):
    N, S = input().split()
    for j in range(len(S)):
        print(S[j] * int(N), end='')

print('')