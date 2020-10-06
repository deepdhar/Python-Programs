# pattern      		   *
#			  * *
#			 * * *
#			* * * *
n=4
for i in range(1,n):
	print(" " * (n-i) + "* " * i)





	
# program to count special characters in a string
str1 = input()
p = ",.@#$%^&*()[]<>/+=-_`~ "
count=0

for ch in str1:
	if ch in p:
		count += 1
print(count)








#program to count vowels and consonants of a string
str1 = input()
vowels = "aeiou"
count1 = 0
count2 = 0

for ch in str1.lower():
	if ch>='a' and ch<='z':
		if ch in vowels:
			count1 += 1
		else:
			count2 += 1
	else:
		continue
print("Vowels: {}\nConsonants: {}".format(count1,count2))







#program to check if a string is plaindrome or not
str1 = "madam"
str2 = str1[::-1]

if str2==str1:
	print("It is palindrome")
else:
	print("It is not palindrome")



	
	
	
	
	
#program to remove space from string
string1 = input()
string2 = string1.replace(" ", "")
print(string2)
