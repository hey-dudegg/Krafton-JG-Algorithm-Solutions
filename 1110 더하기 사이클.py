'''
BOJ 1110번 더하기 싸이클 개요
> 주어진 수 a는 문자열로 입력받는다.
> 원래 a와 연산 뒤의 num이 같아질 때까지 반복하며 횟수를 cycle로 저장한다.
> 같아질 때의 cycle의 값을 출력한다.
'''

a = input()             # 입력받은 수 a는 문자열
num = ""                # 빈 문자열 생성
cycle = 0               # 싸이클 횟수
 
def plus_digit(n : str) -> str:     # 한 자릿수일 때, "0"을 붙여 두 자릿수로 반환
    if len(n) == 1 :
        n = "0" + n
    return n

# 초기 1 싸이클
a = plus_digit(a)        
num = plus_digit(str(int(a[0]) + int(a[1])))    # 문자열-> 정수형 -> 연산 -> 문자열 
num = a[1] + num[1]                 # 처음 숫자의 오른쪽 자릿수 + 연산된 숫자의 오른쪽 자릿 수

# 2회 싸이클부터 연산
while a != num :                    # a과 num가 같지 않을때 반복
    num = plus_digit(num)
    sum_num = plus_digit(str(int(num[0]) + int(num[1])))
    num = num[1] + sum_num[1]
    cycle += 1

print(cycle+1)                      # 초기 싸이클인 1회를 더해준다