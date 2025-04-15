def binary_search(arr, val):
    """Standard binary search to find insertion index in a list of values."""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid
    return left

def library_sort(arr):
    if not arr:
        return []

    n = len(arr)
    # Add extra space for gaps — typically 2n size
    size_with_gaps = 2 * n
    sorted_arr = [None] * size_with_gaps
    actual_positions = []

    # Insert first element in the middle
    mid = size_with_gaps // 2
    sorted_arr[mid] = arr[0]
    actual_positions.append(mid)

    for x in arr[1:]:
        # Build compact array of current values (only filled positions)
        current_vals = [sorted_arr[pos] for pos in actual_positions]
        # Binary search on current sorted values
        idx = binary_search(current_vals, x)

        # Try to find an empty slot near the ideal location
        if idx == len(actual_positions):
            ideal_pos = actual_positions[-1] + 1
            while ideal_pos < len(sorted_arr) and sorted_arr[ideal_pos] is not None:
                ideal_pos += 1
        else:
            ideal_pos = actual_positions[idx]
            while ideal_pos >= 0 and sorted_arr[ideal_pos] is not None:
                ideal_pos -= 1

        # Fallback in case both directions fail (should not happen for 2n size)
        if ideal_pos < 0 or ideal_pos >= len(sorted_arr):
            raise Exception("No space to insert value.")

        # Insert value
        sorted_arr[ideal_pos] = x
        actual_positions.insert(idx, ideal_pos)

    return [sorted_arr[i] for i in actual_positions]
