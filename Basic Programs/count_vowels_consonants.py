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