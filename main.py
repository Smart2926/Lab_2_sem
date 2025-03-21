import unittest

def find_unsorted_subarray(arr):
    n = len(arr)
    if n <= 1:
        return (-1, -1)
    
    left, right = 0, n - 1
    
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1
    
    if left == n - 1:
        return (-1, -1) 
    
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1
    
    subarray_min = arr[left]
    subarray_max = arr[left]
    for i in range(left, right + 1):
        if arr[i] < subarray_min:
            subarray_min = arr[i]
        if arr[i] > subarray_max:
            subarray_max = arr[i]

    while left > 0 and arr[left - 1] > subarray_min:
        left -= 1
    
    while right < n - 1 and arr[right + 1] < subarray_max:
        right += 1
    
    return (left, right)

