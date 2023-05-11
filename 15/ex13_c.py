def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [64, 25, 12, 22, 11]
print ("Original array:" ,arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
