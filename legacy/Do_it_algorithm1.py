# 재귀 알고리즘 분석

def recur(n: int) -> int:
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

x = int(input('정수값을 입력하세요.:'))

recur(x)

# 실습 5-1 양의 정수 n의 팩토리얼 구하기

# def factorial(n: int) -> int:
#     if n > 0:
#         return n * factorial(n - 1)
#     else:
#         return 1
    
# if __name__ == '__main__':
#     n = int(input('출력할 팩토리얼값을 입력하세요.:'))
#     print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')

# 자료구조와 함께 배우는 알고리즘 입문 실습

# # 2-2 시퀀스 원소의 최댓값 출력하기

# from typing import Any, Sequence

# # 시퀀스형 a 원소의 최댓값을 반환, a는 Sequence 타입으로 리턴하고, Any 타입을 return 할 것이다. (주석)
# def max_of(a: Sequence) -> Any:

#     maximum = a[0] # max를 0번째 배열로 선택
#     for i in range(1, len(a)): # 1에서 len(a)까지 반복
#         if a[i] > maximum: maximum = a[i] # a[i] 번째 배열이 max보다 크다면, max에 대입

#     return maximum

# if __name__ == '__main__': # 모듈의 이름을 가지고 있는 변수이다. 현재 .py의 이름을 가지고 있는 변수이다.
#     print('배열의 최댓값을 구합니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num

#     for i in range(num):
#         x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

#     print(f'최댓값은 {max_of(x)}입니다.')


# 1-23오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

# print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
# n = int(input('짧은 변의 길이를 입력하세요.: '))

# for i in range(n):
#     for _ in range(n - i - 1):
#         print(' ', end='')
#     for _ in range(i + 1): # (n - i - 1) + (i + 1) = n을 이용한다.
#         print('*', end='')
#     print()


# 1-22 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

# print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
# n = int(input('짧은 변의 길이를 입력하세요.: '))

# for i in range(n):
#     for j in range(i + 1):
#         print('*', end='')
#     print()


# 1-21 2자리 양수(10~99) 입력받기

# print('2자리 양수를 입력하세요.')

# while True:
#     no = int(input('값을 입력하세요.:'))
#     if no >= 10 and no <= 90: # if not(no < 10 or no > 99):
#         break

# print(f'입력받은 양수는 {no}입니다.')


# 1-20 10 ~ 99 사이의 난수 n개 생성하기(13이 나오면 중단)

# import random

# n = int(input('난수의 개수를 입력하세요.'))

# for i in range(n):
#     r = random.randint(10, 99)
#     print(r, end=' ')
#     if r == 13:
#         print('\n프로그램을 중단합니다.')
#         break

# else:
#     print('\n난수 생성을 종료합니다.')


# 1-17 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기


# area = int(input('직사각형의 넓이를 입력하세요.: '))

# for i in range(1, area + 1):
#     if i * i > area: break
#     if area % i: continue
#     print(f'{i} x {area // i}')


# 1-14 *를 n개 출력하되 w개 마다 줄바꿈하기 1

# print('*을 출력합니다.')
# n = int(input('몇 개를 출력할까요?'))
# w = int(input('몇 개마다 줄바꿈을 할까요?'))

# # 반복문 안에 if문도 밖으로 빼자. 시간을 줄이자.
# # for i in range(n):
# #     print('*', end='')
# #     if (i % w) == w - 1:
# #         print() # 줄바꿈
# for _ in range(n // w):
#     print('*' * w)

# rest = n % w
# if rest:
#     print('*' * rest)

# if n % w:
#     print()


# 1-12 +와 -를 번갈아 출력하기 1,2

# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))

# # 반복문에서 메모리 소요를 줄여야 한다. 또한 상황에 따라 유연하게 수정하기 어렵다.
# # for i in range(n):
# #     if i % 2:
# #         print('-', end='')
# #     else:
# #         print('+', end='')

# # for _ in range(n // 2): # 파이썬에서는 무시하고 싶은 값을 언더스코어로 표현할 수 있다.
# #     print('+-', end='')

# # if n % 2: # n이 홀수인 경우!
# #     print('+')

# print()


# 1-10 a부터 b까지 정수의 합 구하기 1,2

# print('a부터 b까지 정수의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요.:'))
# b = int(input('정수 b를 입력하세요.:'))

# if (a > b):
#     a,b = b,a 

# sum = 0
# # if문은 마지막 단 1번 실행되기 때문에, 따로 빼기
# # for i in range(a, b + 1):
# #     if i < b:
# #         print(f'{i} + ', end = '')
# #     else:
# #         print(f'{i} = ', end = '')
# #     sum += i
# for i in range(a, b): # b까지로 해야 b-1까지 돈다.
#     if i < b:
#         print(f'{i} + ', end = '')
#         sum += i

# print(f'{b} = ', end='')
# sum += b

# print(sum)



# a부터 b까지 정수의 합 구하기(for 문)
# 두 수를 교환할 때 튜플로 묶어서 교환한 뒤 푸는 방식으로 교환 가능하다.

# print('a부터 b까지 정수의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요.:'))
# b = int(input('정수 b를 입력하세요.:'))

# if (a > b):
#     a,b = b,a # a,b를 오름차순으로 정렬한다. 튜플 이용

# sum = 0
# for i in range(a, b + 1):
#     sum += i

# print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')



# 1-8 1부터 n까지 정수의 합 구하기 2(for 문)
# 변수가 하나 있을 땐 for문을 사용하는게 좋다.
# range() 함수로 이터러블 객체 생성하기 
# range(n) : 0 이상 n 미만의 수를 차례대로 나열
# range(a, b, step) : a 이상 b 미만의 수를 step의 간격으로 차례대로 나열


# print('1부터 n까지 정수의 합을 구합니다.')
# n = int(input('n값을 입력하세요.:'))

# sum = 0
# for i in range(1, n + 1 ):
#     sum += i

# print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')


# 1-7 1부터 n까지 정수의 합 구하기 1(while 문)
# print('1부터 n까지 정수의 합을 구합니다.')
# n = int(input('n값을 입력하세요.:'))

# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1

# print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')


# 1-6 pass 문 연습

# n = int(input('정수를 입력하세요.'))

# if n == 1:
#     print('A')
# elif n == 2:
#     print('B')
# elif n == 3:
#     print('C')
# else :
#     pass


# 1-3 입력받은 정수의 부호(양수, 음수, 0) 출력하기

# n = int(input('정수를 입력하세요.:'))

# if n > 0:
#     print('이 수는 양수입니다.')
# elif n < 0:
#     print('이 수는 음수입니다.')
# else:
#     print('이 수는 0입니다.')
    

# 1-2-2 세 정수를 입력받아 중앙값 구하기 2

# def med3(a, b, c):
#     # a가 b보다 크거나 같은 경우, 아래는 c의 위치를 세 곳 중 하나로 정한다.
#     if a >= b: # 'ab' 
#         if b >= c: # ab'c'
#             return b
#         elif a <= c: # 'c'ab
#             return a
#         else:   # acb
#             return c
#     # a가 b보다 작은 경우에서 c의 위치를 결정한다.
#     elif a > c: # 'ba' , ba'c'
#         return a
#     elif b > c: # 'ba', , 앞의 모든 조건들을 불만족( b > a,  c >= a )
#         return c
#     else :
#         return b


# 1-2-1 세 정수를 입력받아 중앙값 구하기 1

# def mod3(a,b,c):
#     if a>=b:
#         if b>=c:
#             return b
#         elif a<=c:
#             return a
#         else:
#             return c
        
#     elif a>c:
#         return a
#     elif b>c:
#         return c
#     else:
#         return b


# a = int(input('a 입력:'))
# b = int(input('b 입력:'))
# c = int(input('c 입력:'))

# print(f'중앙값은 {mod3(a,b,c)}')