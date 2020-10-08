#program to check if a string is palindrome or not
str1 = "madam"
str2 = str1[::-1]

if str2==str1:
	print("It is palindrome")
else:
	print("It is not palindrome")