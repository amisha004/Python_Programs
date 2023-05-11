def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
my_list = [4, 2, 7, 1, 3, 5]
print ("Original array" , my_list)
insertion_sort(my_list)
print ("Sorted array" , my_list)

