def insertion_sort(arr):
    n = len(arr)

    # i-loop increasing, we do j-loop for every element in arr
    for i in range(1, n):
        # j-loop decreasing, checks if current i-element is in the correct spot
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                # swap if order is inproper
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                # break if every element we passed is in the correct order
                break
    return
