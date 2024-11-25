def partition(this_Array, start, end):
    pivot = this_array[end]
    i = start -1
    
    for j in range (start, end):
        if this_array[j] <= pivot :
            i += 1
            this_array[j], this_array[i] = this_array[i],this_array[j]
    this_array[i + 1], this_array[end] = this_array[end], this_array[i + 1]
    return i + 1
    
def quick_sort(this_array,start,end):
    if start < end:
        pi = partition(this_array,start,end)
        quick_sort(this_array, start, pi - 1)
        quick_sort(this_array, pi+1, end)

if __name__ == "__main__":
    this_array = [1,9,2,8,4,6,5]
    print(this_array)
    quick_sort(this_array,0,len(this_array)-1)
    print(this_array)
