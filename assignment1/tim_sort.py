def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        # Shift elements of the sorted subarray that are greater than key
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Place key at the correct position
        arr[j + 1] = key

# Merges two sorted subarrays arr[l..m] and arr[m+1..r]
def merge(arr, l, m, r):
    # Create copies of the subarrays
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]
    
    i = j = 0  # Indexes for L and R
    k = l      # Index for original array

    # Merge back into original array in sorted order
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    # Append any remaining elements from L
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    # Append any remaining elements from R
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        
# Main TimSort function
def tim_sort(arr):
    n = len(arr)
    min_run = 32    # Optimal value found through empirical testing

    # 1: Sort small runs using Insertion Sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # 2: Merge runs in a bottom-up manner
    size = min_run
    while size < n:
        # Pick pairs of runs to merge
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), n - 1)
            # Merge if there are two runs to combine
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2    # Double the run size in each iteration

