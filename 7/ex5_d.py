file = open("test.txt")
f = "test.txt"
a=[] 
b={}
for i in file:
    for j in range(0, len(i)):
        a.append(i[j])

for i in a: 
    if i in b: 
        b[i]+=1 
    else: 
        b[i]=1
        
print(b)
c=f.split(".")
print (c)
if c[1]=="txt":
    print("It is a text file")
elif c[1]=="cpp":
    print("It is a c++ file")
else:
    print("It is a c file")
