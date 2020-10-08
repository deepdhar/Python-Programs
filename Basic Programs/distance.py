# distance between two points

import math

a, b = map(float, input("Enter two points: ").split(" "))
c = math.sqrt(pow(a,2)+pow(b,2))
print("Distance between the two points: " + str(c))