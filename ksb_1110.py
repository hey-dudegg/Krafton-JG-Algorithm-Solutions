"""
str(N[0]+N[-1]) = str(sum). 새로운 수는 str(N[-1]+sum[-1]) = str(new)이다.

0+1 = 1이다. 새로운 수는 11이다.
1+1 = 2이다. 새로운 수는 12이다.

0+6 = 6이다. 새로운 수는 66이다.
6+6 = 12이다. 새로운 수는 62이다.


2+6 = 8이다. 새로운 수는 68이다.

6+8 = 14이다. 새로운 수는 84이다.

8+4 = 12이다. 새로운 수는 42이다.

4+2 = 6이다. 새로운 수는 26이다.
"""

N = str(input())
new = str(N)
cnt = 0

while True:
    # 10보다 작다면
    if int(new) < 10:
        # 일의 자리만 가지고 있는 새로운 수
        # 새로운 수의 마지막 숫자와 새로운 수의 마지막 숫자를 합산
        new = str(new[-1]) + str(new[-1])
    # 10보다 크거나 같다면
    else:
        # 각 자리수의 합
        sum = str(int(new[0]) + int(new[-1]))
        new = str(new[-1]) + str(sum[-1])
    cnt += 1

    # String이 아닌 Int로 비교 시 Index 값과 무관하게 정확한 값 비교 가능
    if int(N) == int(new):
        break

print(cnt)