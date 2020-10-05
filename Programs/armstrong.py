# Program to find armstrong number

def print_armstrong(n, num):
	if n==num:
		return 1
	else:
		return 0

def check_armstrong(num):
	sum=0
	n = num
	while n!=0:
		d = n%10
		sum += d ** 3
		n //= 10
	if print_armstrong(sum, num):
		print("Armstrong")
	else:
		print("Not armstrong")

n = int(input("Enter no.: "))
check_armstrong(n)