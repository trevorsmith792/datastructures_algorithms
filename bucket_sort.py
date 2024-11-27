# Author: TSMITH
# Date: 2024-11-27

def partition(arr, start, end):
    par = arr[end]
    i = start - 1
    for j in range (start, end):
        if (arr[j] < par):
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[end], arr[i + 1] = arr[i + 1], arr[end]
    return i + 1

def quick_sort(arr, start, end):
    if start < end:
        par = partition(arr, start, end)
        quick_sort(arr, start, par - 1)
        quick_sort(arr,par + 1, end)

def bucket_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
        
    buckets = [[] for _ in range (n)]
    
    for num in arr:
        index = int(num * n)
        buckets[index].append(num)
        
    for i in range(n):
        #quick_sort(buckets[i], 0, len(buckets[i]) - 1)
        buckets[i].sort()
        
    result = []
    for bucket in buckets:
        result.extend(bucket)
        
    return result


if __name__ == "__main__":
    arr = [0.42, 0.32, 0.53, 0.51, 0.39, .37, 0.43]
    print(arr)
    sorted_arr = bucket_sort(arr)
    print(sorted_arr)
