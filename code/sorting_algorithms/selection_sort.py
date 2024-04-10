def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    
def smallest_index(lst, start):
    index_min = start
    # find the index of the smallest element
    for i in range(start + 1, len(lst)):
        if lst[i] < lst[index_min]:
            index_min = i
    return index_min

def selection_sort(lst):
    for i in range(len(lst) - 1):
        j = smallest_index(lst, i)
        swap(lst, i, j)
    return lst


# Usage 
arr = [64, 34, 25, 12, 22, 11, 90, 75, 9, 89, 42]
sorted_arr = selection_sort(arr)
print("Sorted array using selection sort:", sorted_arr)
    