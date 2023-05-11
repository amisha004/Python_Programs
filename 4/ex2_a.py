from math import sqrt
pointax1, pointay1  = eval(input('Please enter point a in x y format distance from origin: '))
pointbx2, pointby2  = eval(input('Please enter point b in x y format distance from origin: '))
a= pointbx2 - pointax1
b= pointby2 - pointay1
c=sqrt((a*a)+(b*b))
print("The distance between two point is ",c)
