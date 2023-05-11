def merge_sort(arr):
    # base case: if the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr  
    # divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    # recursively sort the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # merge the sorted halves
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            result.append(left_half[left_index])
            left_index += 1
        else:
            result.append(right_half[right_index])
            right_index += 1      
    result += left_half[left_index:]
    result += right_half[right_index:]
    return result
numbers = [5, 3, 8, 6, 7, 2]
print ("Original array" , numbers)
sorted_numbers = merge_sort(numbers)
print ("Sorted array" , sorted_numbers)

