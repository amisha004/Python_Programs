import math
def ball_collide (x1,y1,r1,x2,y2, r2): 
    dist=math.sqrt((x2-x1)**2+(y2-y1)**2); 
    print("Distance b/w two balls: ",dist) 
    center=dist/2; 
    print("Collision point", center);
    r=r1+r2; 
    print("Sum of radious",r)
    if(center<=r):
        print("They are Colliding")
        return True;
    else:
        print("Not Colliding")
        return False; 
c=ball_collide (5,5,6,2,2,3)
print(c)
c=ball_collide (200,300,40,600,500,50)
print(c)
