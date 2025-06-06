def find_unsorted_subarrays(arr):
    n = len(arr)
    if n <= 1:
        return (-1, -1)

    unsorted_intervals = []
    left = 0

    while left < n - 1:
        if arr[left] > arr[left + 1]:
            right = left + 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1
            unsorted_intervals.append((left, right))
            left = right
        left += 1

    return unsorted_intervals if unsorted_intervals else (-1, -1)
