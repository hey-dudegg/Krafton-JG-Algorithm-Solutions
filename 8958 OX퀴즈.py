n = int(input())

for i in range(n):
    idx = total = 0
    result = input()
    for j in range(len(result)):
        if result[j] == 'O':
            idx += 1
            total += idx
        else:
            idx = 0
    print(total)

"""
n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0  
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)
"""