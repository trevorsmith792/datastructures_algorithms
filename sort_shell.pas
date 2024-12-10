def shell_sort(arr):
    # Start with a large gap, then reduce the gap
    n = len(arr)
    gap = n // 2  # Initial gap value

    # Keep reducing the gap until it becomes 0
    while gap > 0:
        # Perform a gapped insertion sort for this gap size
        for i in range(gap, n):
            # Save the current element to be inserted
            temp = arr[i]
            j = i

            # Shift earlier gap-sorted elements up to make space for the current element
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Insert the current element into its correct position
            arr[j] = temp
        
        # Reduce the gap for the next iteration
        gap //= 2

# Example usage
arr = [12, 34, 54, 2, 3]
print("Original array:", arr)
shell_sort(arr)
print("Sorted array:", arr)
