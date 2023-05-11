def nearly_equal(a, b):
    if abs(len(a) - len(b)) > 1:
        # If the difference in length is more than 1 character, a can't be generated by a single mutation on b
        return False
    
    # Find the index of the first character that is different between the two strings
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    
    if len(a) == len(b):
        # If the strings are the same length, there can only be one different character
        return a[i+1:] == b[i+1:]
    elif len(a) < len(b):
        # If a is shorter than b, there can only be one extra character in b
        return a[i:] == b[i+1:]
    else:
        # If a is longer than b, there can only be one extra character in a
        return a[i+1:] == b[i:]


a = str(input("Enter first string:"))
b =  str(input("Enter first string:"))
if nearly_equal(a, b):
    print("a is nearly equal to b")
else:
    print("a is not nearly equal to b")