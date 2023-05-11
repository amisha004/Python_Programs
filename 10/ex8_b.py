def dup(lst):
    seen = set()
    duplicates = set()
    for x in lst:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    return list(duplicates)
lst = [1, 2, 3, 4, 4, 5, 5, 6]
duplicates = dup(lst)
print("Duplicates:", duplicates)
