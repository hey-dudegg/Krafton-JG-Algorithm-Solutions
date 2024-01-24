arr = [int(x) for x in input().split()]  # 리스트형, [5, 3, 8, 4, 9, 1, 6, 2, 7]

def quick_sort(arr, step_count=[0]):
    if len(arr) <= 1:
        return arr

    step_count[0] += 1
    current_step = step_count[0]

    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []

    # print(f"\nStep {current_step}:")
    # print(f"현재 배열: {arr}")
    # print(f"현재 피벗: {pivot}")

    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    # print(f"피벗을 기준으로 작은 값: {lesser_arr}")
    # print(f"피벗과 같은 값: {equal_arr}")
    # print(f"피벗을 기준으로 큰 값: {greater_arr}")

    result = quick_sort(lesser_arr, step_count) + equal_arr + quick_sort(greater_arr, step_count)

    # print(f"정렬된 결과: {result}")
    return result

# print(f"원본 배열: {arr}")
result = quick_sort(arr)
# print(f"\n최종 정렬 결과: {result}")
