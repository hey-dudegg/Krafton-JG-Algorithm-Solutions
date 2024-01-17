A, B, V = map(int, input().split())

x = (V - B) / (A - B) # 여기가 핵심, V - B를 해야 정상에 올랐을 때 끝난다
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)