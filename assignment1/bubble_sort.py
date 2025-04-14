def bubble_sort(arr):
    n = len(arr)

    for pass_num in range(n):
        swapped = False
        for i in range(n - 1 - pass_num):   
            # Optimized version with the subtraction of pass_num - we just don't check passed elements as they are already sorted
            if arr[i] > arr[i + 1]:
                # here is more "pythonic" version of swapping, without temp variable
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped: 
            # we break when we swapped all  the elements (all elements are in the correct order)
            break
    return 
