def binary_search(arr, val):
    """Standard binary search to find insertion index."""
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid
    return left

def library_sort(arr):
    if not arr:
        return []

    n = len(arr)
    # Choose a gap size (ex, 2n for simplicity)
    size_with_gaps = 2 * n
    sorted_arr = [None] * size_with_gaps

    # Insert first element in the middle
    mid = size_with_gaps // 2
    sorted_arr[mid] = arr[0]
    count = 1

    for x in arr[1:]:
        # Create a compact array of current elements (excluding gaps)
        current = [item for item in sorted_arr if item is not None]
        
        # Perform binary search on current array
        idx = binary_search(current, x)

        # Map to real index in sorted_arr (with gaps)
        real_idx = 0
        nones_seen = 0
        for i in range(len(sorted_arr)):
            if sorted_arr[i] is not None:
                if nones_seen == idx:
                    real_idx = i
                    break
                nones_seen += 1
        else:
            real_idx = len(sorted_arr) - 1

        # Find nearest empty slot to insert
        insert_idx = real_idx
        while insert_idx < len(sorted_arr) and sorted_arr[insert_idx] is not None:
            insert_idx += 1
        if insert_idx == len(sorted_arr):  # Try backwards if no forward space
            insert_idx = real_idx
            while insert_idx >= 0 and sorted_arr[insert_idx] is not None:
                insert_idx -= 1
            if insert_idx < 0:
                raise Exception("No space to insert")

        sorted_arr[insert_idx] = x
        count += 1

    # Filter out None and return sorted array
    return [x for x in sorted_arr if x is not None]

