a, b = 1, 2
total = 0
print (a, end =' ')
while (a <= 2000000-1):
        if a % 2 != 0:
                total = total + a
        a, b = b, a+b
        print (a, end =' ')
print ("\n Sum of prime numbers term in fibonacci series = ", total)

