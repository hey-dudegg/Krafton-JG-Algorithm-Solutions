"""
# 틀린 답안(EOFError)
max = 0
index = 1

for i in range(10):
    num = int(input(""))
    if num in range(1,101):
        if num > max: 
            max, num = num, max
            index = i

print(max)
print(index)
"""

list = []

for i in range(9): # range(10)이면 0부터 9까지 10번 받는다!
    list.append(int(input("")))
    
print(max(list))
print(list.index(max(list)) + 1) # 인덱스는 0부터 시작한다!