import time
print ("")
time.sleep(0.5)
print ("Hello avid coder!")
print ("")
time.sleep(1)
print ("You find yourself in the Jobcentre talking with your work agent")
print ("")
time.sleep(2.5)
print ("As you are mulling over the possibilities you mention your passion for coding and the work agents eyes light up!")
print ("")
time.sleep(2.5)
print ("'There is a fantastic opportunity that has just opened up at CodeNation, they'd like to meet with you immediately'")
print ("")
time.sleep(2.5)
print ("You contain your excitement and quickly remember you aren't the most proficient with directions and mention it to the work agent")
print ("")
time.sleep(2)
print ("The agent produces a smirk and says:")
print ("")
time.sleep(2)
print ("'Not to worry adventurer! The great people of Manchester will help guide you to your destination, all you have to do is answer some trivia questions'")
print ("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
time.sleep(2)
print ("The rules of the game are as follows: Arrive at CodeNation with the most amount of time left on the clock")
print ("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
time.sleep(2)
print ("1. You will be tracked real-time on how long it takes you to reach the destination.")
time.sleep(2)
print ("2. The timer will begin as soon as you leave the Jobcentre.")
time.sleep(2)
print ("3. There will be points where you decide to turn left or right, it's possible to take a wrong turn and end up lost, resulting in you losing the game.")
time.sleep(2)
print ("4. At times you may enter into two types of randoms events, one giving you a chance to return to the right path by answering a question and the other      resulting in an unfortunate loss")
import sys

print("")
time.sleep(1)
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
print_slow("GOOD LUCK!")