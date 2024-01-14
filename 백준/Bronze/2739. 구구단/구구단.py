num = int(input(""))

if num > 0 and num < 10: 
    i = 1 # 시작 조건
    while i < 10: # 종결 조건
        print(f"{num} * {i} = {num * i}")
        i += 1 # 반복