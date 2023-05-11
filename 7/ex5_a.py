string = input("Enter a string: ")
print("The length of the string is:", len(string))

mydict = {}
for i in range(len(string)):
    char = string[i]
    print(i+1, char)
    if char in mydict:
        mydict[char] += 1
    else:
        mydict[char] = 1

print("Dictionary is:", mydict)
