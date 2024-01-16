num = int(input(""))
"""
for문의 기본 구조
for 변수 in 리스트(or 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
"""

# if num > 0 and num < 10: # for문 52ms
#     for i in range(1,10):
#         print(f"{num} * {i} = {num * i}")

if num > 0 and num < 10: # while문 44ms
    i = 1 # 시작 조건
    while i < 10: # 종결 조건
        print(f"{num} * {i} = {num * i}")
        i += 1 # 반복