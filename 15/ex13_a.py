def linear_Search(list1, n, key):
    for i in range(0, n):
        if (list1[i] == key):
            return i
    return -1
A=[]
elements= int(input("Enter number of elements in the list: "))
for i in range(elements):
    print("Enter the " + str(i) +" element")
    A.append(int(input()))
key = int(input("Enter the number to find in list: "))
res = linear_Search(A, elements, key)
if(res == -1):
    print("Name not found")
else:
    print("Name found at index: ", res)
