def binary_search(item_list,item):
    first = 0
    last = len(item_list)-1
    found = False
    while( first<=last and not found):
        mid = (first + last)//2
        if item_list[mid] == item :
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
A=[]
print("Enter number of elements in the list")
elements= int(input())
for i in range(elements):
    print("Enter the " + str(i) +" element")
    A.append(int(input()))
print("Enter the number to find in list")
key = int(input())
result = str(binary_search(A, key))
if(result=="False"):
    print("Number in the List")
else:
    print("Number not in the List")
