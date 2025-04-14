def merge_sort(arr):
    n = len(arr)

    # Base case: if the array has only one element, it's already sorted
    if n == 1:
        return arr

    # Divide the array into two halves
    mid = n // 2
    L = arr[:mid]
    R = arr[mid:]

    # Recursively sort both halves
    L = merge_sort(L)
    R = merge_sort(R)

    # Initialize pointers for both halves and the merged array
    l, r = 0, 0
    L_len = len(L)
    R_len = len(R)
    i = 0

    # Initialize the array to store the merged result
    sorted_arr = [0] * n

    # Merge the two sorted halves into sorted_arr
    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1

    # Copy any remaining elements from L (if any)
    while l < L_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    # Copy any remaining elements from R (if any)
    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    return sorted_arr
