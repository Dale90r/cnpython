#What is Minestrone?

multiple_choice = [
    "A):Potato",
    "B):Noodles",
    "C):Soup",
    "D):Cheese",
]

print('What is minestrone?')

choices = (multiple_choice)
print(*choices, sep = "\n") 
 
answer = input()
if answer == "c" or answer == "C":
    print(answer, "is correct!")
elif answer == "soup" or answer == "Soup":
    print(answer, "is correct!")
else:
    print(answer, "is not correct!")

#------------------------------------------------------------------
#Mojito is a traditional cocktail from?

country_list = [
    "A):Italy",
    "B):Spain",
    "C):Mexico",
    "D):Cuba",
]

print('The Mojito is a traditional rum cocktail from which country?:')

choices = (country_list)
print(*choices, sep = "\n")

answer = input()
if answer == "d" or answer == "D":
    print(answer, "is correcto!")
elif answer == "cuba" or answer == "Cuba":
    print(answer, "is correcto!")
else:
    print(answer, "is not correct!")
#------------------------------------------------------------------
#In the Marvel cinematic universe, what is the name of Thors home planet
answer = input("In the Marvel cinematic universe, what is the name of Thors home planet?:")
if answer == "Asgard" or answer == "asgard":
    print(answer, "is the correct answer!")
else:
    print(answer, "is incorrect!")
#------------------------------------------------------------------
#Computer terminology question
answer = input("In computer terminology what does the acronym 'LAN' stand for?:")
if answer == "Local Area Network" or answer == "local area network":
    print(answer, "is the correct meaning, well done!!")
elif answer == "LOCAL AREA NETWORK" or answer == "Local area network":
    print(answer, "is the correct meaning, well done!!")
else:
    print("sorry," + answer, ("is incorrect"))
#------------------------------------------------------------------
#Highest mountain located in which mountain range?
answer = input("The highest montain on Earth is located in which mountain range?:")
if answer == "The Himalayas" or answer == "the himalayas":
    print(answer, "is the correct answer!") 
elif answer == "Himalayas" or answer == "himalayas":
    print(answer, "is the correct answer!")
else:
    print("sorry," + answer, ("is incorrect"))
#-------------------------------------------------------------------
#located halfway between iceland and norway, the Faroe islands belong to which country?