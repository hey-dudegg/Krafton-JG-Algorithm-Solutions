a = input()             # 입력받은 수 a는 문자열
num = ""
cnt = 0

if len(a) == 1 :
    a = "0" + a         # 0이 한 자리수일 때 두 자리수로 변환
num = str(int(a[0]) + int(a[1]))
if len(num) == 1 :
    num = "0" + num
num = a[1] + num[1]     # 초기 1회

while a != num :        # num과 a가 같지 않을때 반복
    if len(num) == 1 :
        num = "0" + num
    sum_num = str(int(num[0]) + int(num[1]))
    if len(sum_num) == 1 :
        sum_num = "0" + sum_num
    num = num[1] + sum_num[1]
    cnt += 1

print(cnt+1)
#    if a == num:
#        print(num)
#        break



