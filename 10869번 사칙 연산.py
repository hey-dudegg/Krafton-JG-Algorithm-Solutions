'''
아래의 코드를 한 줄로 해결하기
a, b = map(int, input().split())
print(a)
print(type(a))

a, b = input().split() # 변수에 먼저 문자열로 숫자를 저장한다
a = int(a) # 이후 문자열인 숫자를 정수형으로 형변환한다.
b = int(b)
'''

a, b = map(int, (input("").split()))
print(f"{a+b}")
print(f"{a-b}")
print(f"{a*b}")
print(f"{a//b}")
print(f"{a%b}")
