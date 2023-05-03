def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    sorted_arr = []
    i, j = 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1
    sorted_arr += left_half[i:]
    sorted_arr += right_half[j:]
    
    return sorted_arr

my_list = [4, 6, 1, 8, 3, 9, 2, 5, 7]
sorted_list = merge_sort(my_list)
print(sorted_list)