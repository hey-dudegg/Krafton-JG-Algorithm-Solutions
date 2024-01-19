#1110
start_num = int(input())
cur_num = start_num
cycle_count = 0

# 첫 번째 사이클: while 조건을 만족하기 위해 따로 실행
# 새 숫자의 10의자리 수 = 현재 숫자의 1의자리 수
def cycle(cur_num):
    ten_number = cur_num % 10
    # 새 숫자의 1의자리 수 = (현재 숫자의 자릿수 합)의 1의자리 수
    one_number = (cur_num // 10 + cur_num % 10) % 10
    cur_num = 10 * ten_number + one_number # 새로운 수
    global cycle_count
    cycle_count += 1
    return cur_num

cycle(cur_num)

while cur_num != start_num:
  # 처음 숫자가 나올 때까지 반복
  cur_num = cycle(cur_num)

print(cycle_count)