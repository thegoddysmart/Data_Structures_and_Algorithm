def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i
        
        while j > 0 and key < lst[j-1]:
            lst[j] = lst[j-1]
            j -= 1
            
        lst[j] = key
    return lst
        
# Usage
arr = [64, 34, 25, 12, 22, 11, 90, 75, 9, 89]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)