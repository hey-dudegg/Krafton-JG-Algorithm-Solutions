arr = [int(x) for x in input().split()]  # 리스트형, [5, 3, 8, 4, 9, 1, 6, 2, 7]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []

    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    result = quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

    return result

result = quick_sort(arr)
