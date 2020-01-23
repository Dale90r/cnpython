#what is 15 percent of 2000?
answer = int(input('What is fifthteen percent of two thousand?:'))
if answer == 300:
    print("Congratulations that is the correct answer!")
else:
    print("Sorry that answer is not correct")
#-----------------------------------------------------------------------------------------------------|
#which number has the same amount of letter as its numerical value?
answer = int(input("Which number as a word has the same amount of letters as it's numerical value?:"))
if answer == 4:
    print("Well done, thats the right answer!")
else:
    print("Ooops, unfortunately that answer is not correct")
#-------------------------------------------------------------------------------------------------------|
#the first written number to contain the letter a?
answer = input ('In the English language, What is the first number to contain the letter "a"?:') 
if answer == 'one thousand' or answer == ("1000"): 
    print('That is correct, one thousand is the first numerical as a word to contain the letter "a"' )
else:
    print("That", (answer) ,"is not correct")
#--------------------------------------------------------------------------------------------------------|
#what comes next after million, billion and trillion?
multiple_choice = [
    'A):Quintillion',
    'B):Quadrillion',
    'C):Sextillion',
    'D):Septillion',
]
print('What comes next after million, billion and trillion?:')
choices = (multiple_choice )
print(*choices, sep = "\n") 
answer = input()
 
if answer == "B" or answer == "b":
    print("Quadrillion is correct")
elif answer == "Quadrillion" or answer == "quadrillion":
    print(answer, ("is correct!"))
elif answer == "QUADRILLION":
    print(answer, ("is correct!"))
else:
    print(answer, ("is not correct"))
#--------------------------------------------------------------------------------------------------------|
#A shape with 8 sides is called Octagon OR an Octagon? 
answer = input ("A shape with eight sides is called Octagon or an octagon?")
if answer == "An octagon" or answer == "an octagon":
    print(answer, "is the right answer!") 
elif answer == "Octagon" or answer == "Octagon":
    print(answer, "No, no, no, thats the name of the ring UFC fighters fight in")
else:
    print(answer, "is incorrect!!")
#--------------------------------------------------------------------------------------------------------|
#Square root of 36
import math
answer = int(input("What is the square root of thirty six?"))
math.sqrt(36)
if answer == math.sqrt(36):
    print(answer, ("is correct!"))
else:
    print(answer, ("is incorrect!!"))
#Function to check if number is prime
def check(n): 
    if n == 1: 
        return False
          
        
    for x in range(2, (int)(math.sqrt(n))+1): 
        if n % x == 0: 
            return False 
    return True
  
n = answer
if check(n): 
    print(answer,"is also a prime number")  
else: 
    print(answer,"is not a prime number") 
#----------------------------------------------------------------------------
