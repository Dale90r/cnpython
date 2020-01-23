number = 519
orig = number
rev = 0
   
while number > 0:
    rev = (rev*10) + number%10
    number //= 10
if orig == rev:
    print(orig, "is a Palindrome Number.")
else:
    print(orig, "is not a Palindrome Number.")

