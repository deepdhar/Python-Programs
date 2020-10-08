# GCD of two numbers

a,b = map(int, input("Enter two numbers: ").split(" "))
gcd = 0
i = 1

while (i<=a and i<=b):
    if (a%i==0 and b%i==0):
        gcd = i
    i += 1
    
print("GCD is: " + str(gcd))