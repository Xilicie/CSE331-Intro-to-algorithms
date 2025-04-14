def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the current index holds the smallest value
        min_index = i

        # Search for the smallest value in the rest of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the smallest found value with the value at index i
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return
