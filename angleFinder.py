import math
a= int(input())
b= int(input())
c= math.sqrt(a*a+b*b)
c=c/2
lower=b/2
print (str(int(round(math.degrees(math.acos(lower/c)))))+"°")
