#prime no. from 1 to 100

def prime(n):
    i=2
    while i<=n/2:
        if n%i==0:
            break
        i += 1
    
    if i>n/2:
        return 1
    else:
        return 0

for i in range(1, 101):
    if (prime(i)):
        print(i)