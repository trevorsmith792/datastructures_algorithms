# Helper function to perform insertion sort on small subarrays
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge function to merge two sorted subarrays
def merge(arr, left, mid, right):
    # Create temporary subarrays for merging
    len1, len2 = mid - left + 1, right - mid
    left_subarray = arr[left:left + len1]
    right_subarray = arr[mid + 1:mid + 1 + len2]
    
    # Merge the temporary subarrays back into the original array
    i = j = 0
    k = left
    while i < len1 and j < len2:
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            j += 1
        k += 1
    
    # If there are any remaining elements in left_subarray
    while i < len1:
        arr[k] = left_subarray[i]
        i += 1
        k += 1
    
    # If there are any remaining elements in right_subarray
    while j < len2:
        arr[k] = right_subarray[j]
        j += 1
        k += 1

# Timsort function
def timsort(arr):
    min_run = 32
    
    # Step 1: Sort small subarrays of size 'min_run' using insertion sort
    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, n - 1))
    
    # Step 2: Merge subarrays of increasing size
    size = min_run
    while size < n:
        for start in range(0, n, 2 * size):
            mid = min(n - 1, start + size - 1)
            end = min((start + 2 * size - 1), n - 1)
            if mid < end:
                merge(arr, start, mid, end)
        size *= 2

# Example usage:
arr = [5, 21, 7, 23, 19, 13, 3, 9, 12, 18]
print("Original array:", arr)
timsort(arr)
print("Sorted array:", arr)
