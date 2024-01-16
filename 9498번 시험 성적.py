score = int(input(""))

# if score > -1 and score < 101: # 44ms로 시간은 같다.
if score >= 0 and score <= 100 :
    if score > 89 :
        print("A")
    elif score > 79 :
        print("B")
    elif score > 69 :
        print("C")
    elif score > 59 :
        print("D")
    else:
        print("F")