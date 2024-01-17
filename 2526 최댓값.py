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

    
