
"""
# 내포 표기 생성으로 리스트 생성
arr = [int(x) for x in input().split()] # 리스트형, [21, 10, 12, 20, 25, 13, 15, 22]

def merge_sort(arr):
    if len(arr) < 2: # 배열의 길이가 1인 경우
        return arr # 정렬된 상태로 판단
    
    mid = len(arr) // 2 # 리스트의 중간 찾기
    low_arr = merge_sort(arr[:mid]) # 중간으로 나눈 왼쪽 배열을 재귀적으로 끝까지 분할
    high_arr = merge_sort(arr[mid:]) # 나머지 오른쪽 배열도 끝까지(부분 배열의 길이가 1) 분할
    # --- 분할 과정 종료 ---

    merged_arr = [] # 정렬한(정복한) 배열을 최종적으로 담는 배열 생성
    l = h = 0

    while l < len(low_arr) and h < len(high_arr):
        
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

print(merge_sort(arr))
"""
# 내포 표기 생성으로 리스트 생성
arr = [int(x) for x in input().split()] # 리스트형, [21, 10, 12, 20, 25, 13, 15, 22]

def merge_sort(arr, step_count=[0]):
    if len(arr) < 2: # 배열의 길이가 1인 경우
        return arr # 정렬된 상태로 판단
    
    mid = len(arr) // 2 # 리스트의 중간 찾기
    low_arr = merge_sort(arr[:mid], step_count) # 중간으로 나눈 왼쪽 배열을 재귀적으로 끝까지 분할
    print(f"\n재귀 직전의 배열: {arr}")
    print(f"재귀 후 반환 low배열: {low_arr}")

    high_arr = merge_sort(arr[mid:], step_count) # 나머지 오른쪽 배열도 끝까지(부분 배열의 길이가 1) 분할
    print(f"재귀 후 반환 high배열: {high_arr}")
    # --- 분할 과정 종료 ---
    
    step_count[0] += 1
    current_step = step_count[0]
    
    merged_arr = [] # 정렬한(정복한) 배열을 최종적으로 담는 배열 생성
    l = h = 0 # merged 배열에 low와 high의 요소를 추가할 때 참고할 인덱스, 배열의 요소가 1개일 때는 0으로 초기화

    print(f"\nStep {current_step}:")

    # Step 3부터 h의 요소가 2개이므로 [21, 10] 뒤인 [2]에 추가 가능하다.
    while l < len(low_arr) and h < len(high_arr): 
        if low_arr[l] < high_arr[h]: # 배열의 맨 앞 요소의 대소 비교
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    print(f"low_arr의 l 인덱스: {l}")
    print(f"high_arr의 h 인덱스: {h}")

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    print(f"병합된 배열: {merged_arr}")
    return merged_arr

print(f"원본 배열: {arr}")
result = merge_sort(arr)
print(f"\n최종 정렬 결과: {result}")
