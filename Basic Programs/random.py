import random

a,b = map(int, input("Enter a and b: ").split(" "))
c = random.randint(a,b)
print("Random no. between a and b: " + str(c))