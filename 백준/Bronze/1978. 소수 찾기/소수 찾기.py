n = int(input())
numbers = map(int, input().split())
# 전달받은 값을 int() 함수에 적용한 결과를 input().split()으로 반환한다.
sosu = 0
for num in numbers:
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
        if error == 0:
            sosu += 1
print(sosu)