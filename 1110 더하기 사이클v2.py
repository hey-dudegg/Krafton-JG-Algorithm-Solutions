cur = num = int(input())
ten = cur // 10
one = cur % 10
cnt = 0

new = (ten + one) % 10
cur = one * 10 + new
cnt += 1

while cur != num:
    ten = cur // 10
    one = cur % 10
    new = (ten + one) % 10
    cur = one * 10 + new
    cnt += 1

print(cnt)