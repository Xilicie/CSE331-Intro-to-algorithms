def insertion_sort(arr):
    n = len(arr)

    # Start from the second element and iterate through the array
    for i in range(1, n):
        # Compare the current element with the ones before it, moving backward
        for j in range(i, 0, -1):
            # If the element before is greater, swap them
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                # Stop if elements are in correct order (no more shifting needed)
                break
    return
