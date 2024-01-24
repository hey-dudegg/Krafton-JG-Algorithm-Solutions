from itertools import permutations
import sys

input = sys.stdin.readline
a = []
n, m = map(int, input().split())

result = map(lambda x: ' '.join(map(str, x)), permutations(range(1, n + 1), m))
for x in result:
    print(x)
