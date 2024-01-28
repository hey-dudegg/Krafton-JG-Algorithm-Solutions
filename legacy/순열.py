list = [1,2,3,4,5]
used = [0] * len(list)

def perm(arr, n):
    if n == len(list):
        print(arr)
        return
    
    for i in range(len(list)):
        if not used[i]:
            used[i] = 1
            arr.append(list[i])
            perm(arr, n+1)
            arr.pop()
            used[i] = 0

perm([], 0)