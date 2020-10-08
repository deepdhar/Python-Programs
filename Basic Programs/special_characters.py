# program to count special characters in a string
str1 = input()
p = ",.@#$%^&*()[]<>/+=-_`~ "
count=0

for ch in str1:
	if ch in p:
		count += 1
print(count)