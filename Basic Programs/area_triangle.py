# area of a triangle

import math

a,b,c = map(float, input("Enter three sides of the triangle: ").split(" "))
p = (a+b+c)/2

area = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Area of triangle: " + str(area))