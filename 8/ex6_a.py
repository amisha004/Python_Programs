f=input("Enter file name: ") 
for line in reversed (list (open(f))):
    print(line.rstrip()[::-1])
