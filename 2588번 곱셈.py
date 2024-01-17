a = int(input()) # 문자열 -> 정수형
b = input() # 문자열
# print(b[-1])
# 문자열도 인덱싱이 가능하다. 맨 뒤는 -0이 아닌 -1이다.


for i in range(3):
    print(a * int(b[-(i+1)])) # 인덱싱한 b의 요소는 아직 문자열이다. 형변환하자

print(a*int(b))