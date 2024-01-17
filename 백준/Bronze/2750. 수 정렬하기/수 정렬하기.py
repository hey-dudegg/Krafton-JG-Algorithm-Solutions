n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    arr.append(num)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    low_arr, equal_arr, high_arr = [], [], []

    for num in arr:
        if num < pivot:
            low_arr.append(num)
        elif num == pivot:
            equal_arr.append(num)
        else:
            high_arr.append(num)

    result = quick_sort(low_arr) + equal_arr + quick_sort(high_arr)

    return result

merged_arr = quick_sort(arr)

for i in range(len(merged_arr)):
    print(merged_arr[i])

# for n in merged_arr:
#    print(n)
