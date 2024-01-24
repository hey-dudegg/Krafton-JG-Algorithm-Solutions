'''
arr = []

for _ in range(9):
    dwf = int(input())
    arr.append(dwf)
arr.sort()

sum = sum(arr)
fake = []

for i in range(9):
    for j in range(i+1, 9):
        if(len(fake) == 2):
            break
        if sum - arr[i] - arr[j] == 100:
            fake.append(arr[i])
            fake.append(arr[j])

for i in arr:
    if i in fake:
        continue
    print(i)
'''
'''
from itertools import combinations

arr = []
for _ in range(9):
    dwf = int(input())
    arr.append(dwf)
arr.sort()

for i in combinations(arr, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
'''
dwf = [int(input()) for _ in range(9)]
seven = []

def dfs(depth, start):
    if depth == 7:
        if sum(seven) == 100:
            for j in sorted(seven):
                print(j)
            exit()
        else:
            return
        
    for i in range(start, len(dwf)):
        seven.append(dwf[i])
        dfs(depth + 1, i + 1)
        seven.pop()

dfs(0, 0)