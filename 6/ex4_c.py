# By considering the terms in the Fibonacci sequence whose values do not exceed 100
# find the sum of the even-valued terms.

flag = 8 # Setting the number of the iteration.
a = 1
b = 2
temp = 0
sum = 2
print("The Fibonacci sequence is :")
print(" \n",a," \n",b)
while(flag>=0):
	temp = a + b
	a = b
	b = temp
	if(temp % 2 == 0):
		sum = sum + temp
	flag = flag - 1
print("The sum of even number in Fibonacci is : \n",sum)
