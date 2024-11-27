

def merge(left,right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    i = len(arr) // 2
    left_half = arr[:i]
    right_half = arr[i:]
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted,right_sorted)

if __name__ == "__main__":
    # Example usage:
    arr = [1,4,2,9,6,4,3,22,0,2]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
