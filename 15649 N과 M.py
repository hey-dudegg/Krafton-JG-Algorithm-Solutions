from itertools import permutations
import sys

input = sys.stdin.readline
a = []
n, m = map(int, input().split())

result = map(lambda x: ' '.join(map(str, x)), permutations(range(1, n + 1), m))
for x in result:
    print(x)

'''
import sys
input = sys.stdin.readline

def back_trk():
    if m == len(a):
        print(" ".join(map(str, a)))
        return
    
    for i in range(1, n + 1):
        if i not in a:
            a.append(i)
            back_trk()
            a.pop()

a = []
n, m = map(int, input().split())

back_trk()
'''


