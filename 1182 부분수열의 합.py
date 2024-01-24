from itertools import combinations
import sys

input = sys.stdin.readline
n, s = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
cnt = [0]
for i in range(1, n + 1): 
    # n = 1인 경우도 포함, 총 5번 돌아야 하기 때문에 n + 1까지
    comb = combinations(arr, i)
    # itertools.combinations object를 반환한다. 리스트나 튜플로 변환해서 사용해야 한다.
    for x in comb:
        # for문을 통해 x로 튜플을 꺼내서 합해야 한다.
        if sum(x) == s:
            # sum() 안에 매개변수를 받아야 합계산이 가능하다
            cnt[0] += 1
        
print(cnt[0])