a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)
# 1511001
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(result)):
    idx = int(result[i])
    arr[idx] += 1
for j in range(10):
    print(arr[j])
