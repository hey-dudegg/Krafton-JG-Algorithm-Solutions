year = int(input())

def is_Yoon(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return 1
        else:
            return 0
    else:
        return 0
    
print(is_Yoon(year))