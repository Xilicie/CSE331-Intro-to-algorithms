import math

def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def heapify(arr, n, i, start):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[start + l] > arr[start + largest]:
        largest = l
    if r < n and arr[start + r] > arr[start + largest]:
        largest = r

    if largest != i:
        arr[start + i], arr[start + largest] = arr[start + largest], arr[start + i]
        heapify(arr, n, largest, start)

def heapsort(arr, start, end):
    n = end - start + 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, start)
    for i in range(n - 1, 0, -1):
        arr[start], arr[start + i] = arr[start + i], arr[start]
        heapify(arr, i, 0, start)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def introsort_util(arr, start, end, maxdepth):
    size = end - start + 1
    if size < 16:
        insertion_sort(arr, start, end)
    elif maxdepth == 0:
        heapsort(arr, start, end)
    else:
        pivot = partition(arr, start, end)
        introsort_util(arr, start, pivot - 1, maxdepth - 1)
        introsort_util(arr, pivot + 1, end, maxdepth - 1)

def introsort(arr):
    depth_limit = 2 * math.floor(math.log2(len(arr)))
    introsort_util(arr, 0, len(arr) - 1, depth_limit)
