#Find Angle MBC Challenge
#This program accepts two lines of input - the lengths of sides
#AB and BC of right triangle ABC. Then, hypotenuse AC is calculated,
#and the midpoint of AC, M, is used to establish a new triangle, MBC.
#Finally, angle MBC is calculated and printed in degrees.

import math

#The first side
lineAB = float(input())

#The second side
lineBC = float(input())

#The length of the hypotenuse is equal to the square root of
#the squares of the lengths of the other two sides.
lineAC = math.hypot(lineAB, lineBC)

#The midpoint is half of the length of the hypotenuse.
#In a right triangle, the median drawn to the hypotenuse has the
#length of half of the hypotenuse. Therefore:
lineBM = lineAC / 2

#Find the angle of MCB. Cast the result of acos to degrees.
#angleMCB = math.degrees(math.acos(lineAB / lineAC))

#To find the size of angle MBC, we find the median of BC, calling it E.
lineBE = lineBC / 2

#With midpoint E, there is a new right triangle created within triangle MBC.
#Then, the angle AED is 90 degrees.
#So to find the angle MBC (equal to angle MBE), we use the acos function.
#We cast the answer to degrees, round to the nearest
#integer value, and print the result.
angleMBC = math.degrees(math.acos(lineBE / lineBM))

print ("%r°" % (int(round(angleMBC))))
