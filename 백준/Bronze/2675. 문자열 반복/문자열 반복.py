T = int(input())

for _ in range(T):
    R, word = input().split()
    for x in word:
        print(x*int(R), end='') # end = ''공백으로 구분
    print() # 줄 넘김