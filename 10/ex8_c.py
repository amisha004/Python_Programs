def unique(lst):
    unique_lst = []
    for x in lst:
        if x not in unique_lst:
            unique_lst.append(x)
    return unique_lst
lst = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_lst = unique(lst)
print("Unique elements:", unique_lst)


