# special number
# sum of digits + product of digits of a number = that number

def sod(num):
	if num==0:
		return 0
	else:
		return(num%10 + sod(num//10))

def pod(num):
	if num==0:
		return 1
	else:
		return(num%10 * pod(num//10))

def special_num(n):
	s=sod(n)
	p=pod(n)
	if (s+p) == n:
		print("It is a special number")
	else:
		print("It is not a special number")


n = int(input())
special_num(n)
