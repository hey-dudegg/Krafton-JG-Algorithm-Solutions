n = input() # 1st -'26'
input_length = len(n)   # 2nd - len(2)
array = []  # []
answer = [] # []

#무한 루프에서 빠져나오질 못함: 디버깅 실패
while True:
    if n in answer: 
        break
    for i in range(input_length):   # 3th , 6th, 17th - input_length는 이전 반복에서 '고정'된 2입니다. 여기서 무한 반복이 시작됩니다.
        if input_length <= 1:       
            array.append('0')       
            array.append(n[i])      
        else:                       # 4th
            array.append(n[i])      # 5th - arr = ['2'], 7th - ['2','6'], 18th - array = ['2'], 19th - array = ['2', '6']
                                    # 20th 무한 루프 시작, 26(n[0]n[1], 초기 1회) -> 2 + 6 -> 08 -> 68(n[1]new_data[1], 이후 2회부터~) -> 6 + 8 -> 14 이어야 해서 새로운 반복문 작성하셔야 합니다.
    sum_result = int(array[0]) + int(array[1])  # 8th - 2+6 = 8
    if sum_result >= 10:            
        array.append(str(sum_result)[0])        
        array.append(str(sum_result)[1])        
    else:                                       # 9th
        array.append(str(sum_result))           # 10th - arr = ['2','6','8'] 

    if len(array) == 3:                 # 11th
        new_data = array[1] + array[2]  # 12th - new_data = ['6','8']
    else:                           
        new_data = array[1] + array[3]  

    if new_data == '00':                # ''은 문자열이고, new_data는 리스트입니다. data type 에러 예상됩니다.
        answer.append('0')              # '00'일 때 '0'을 추가한다는 코드의 의미를 잘 모르겠습니다.
    else:                               # 13th
        answer.append(new_data)         # 14th ans = ['6', '8'], 20th ans = ['6', '8', '4']

    print(*answer)                      # 패킹하시면 리스트의 요소가 '문자열'형으로 반환됩니다.('68')
    print(type(*answer))

    input_length = len(new_data)        # 15th - len(2)
    array = []                          # 16th - array = []

print(len(answer) + 1)