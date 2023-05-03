def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left_half = [x for x in arr[:-1] if x <= pivot]
    right_half = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left_half) + [pivot] + quick_sort(right_half)

my_list = [4, 6, 1, 8, 3, 9, 2, 5, 7]
sorted_list = quick_sort(my_list)
print(sorted_list)