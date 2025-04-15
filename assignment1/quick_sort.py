def quick_sort(arr):
    # Base case: if the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose the last element as the pivot
    p = arr[-1]

    # Partition: elements less than or equal to pivot go to L, others to R
    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]

    # Recursively sort left and right subarrays
    L = quick_sort(L)
    R = quick_sort(R)

    # Combine: return sorted left + pivot + sorted right
    return L + [p] + R

