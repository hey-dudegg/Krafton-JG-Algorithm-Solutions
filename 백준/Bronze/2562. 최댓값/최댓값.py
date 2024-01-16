list = []

for i in range(9): # range(10)이면 0부터 9까지 10번 받는다!
    list.append(int(input("")))
    
print(max(list))
print(list.index(max(list)) + 1) # 인덱스는 0부터 시작한다!