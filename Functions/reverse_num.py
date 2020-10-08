#reverse of a number
import math

def reverse_num(n):
    d=int(math.log10(n))
    if n<10:
        return n
    else:
        return (n%10*math.pow(10,d) + reverse_num(n//10))

num = int(input())
print("Reverse:", int(reverse_num(num)))