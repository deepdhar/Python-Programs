# pattern      *
#			  * *
#			 * * *
#			* * * *
n=4
for i in range(1,n):
	print(" " * (n-i) + "* " * i)
