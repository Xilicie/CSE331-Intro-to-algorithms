def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr

    mid = n // 2
    L = arr[:mid]
    R = arr[mid:]

    L = merge_sort(L)
    R = merge_sort(R)

    l, r = 0, 0
    L_len = len(L)
    R_len = len(R)
    i = 0

    sorted_arr = [0] * n

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1
    
    while l < L_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1
    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1
    return sorted_arr
