def reverse(lst):
    i = 0
    j = len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i = i + 1
        j = j - 1
    return lst
lst = [1, 2, 3, 4, 5]
reversed_lst = reverse(lst)
print("Reversed list:", reversed_lst)
