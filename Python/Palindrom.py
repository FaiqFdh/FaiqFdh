""" UNTUK MEREVERSE KATA/String
s = "faiq"[::-1]
print(s)
"""
# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]

# Driver code
s = "racecar"
ans = isPalindrome(s)

if ans:
	print("Yes , It is Palindrom")
else:
	print("No , It is not Palindrom")
