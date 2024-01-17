'''
c = int(input())

for _ in range(c):
    idx = sum = 0
    n = list(map(int, input().split()))
    num = n[0]
    for i in range(num-1):
        sum += int(n[i+1])
    avg = sum / n[0]
    for j in range(num-1):
        if n[j+1] > avg:
            idx += 1
    print(f"{avg}%")
'''
n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1
    rate = cnt/nums[0] * 100
    print(f'{rate:.3f}%')