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
import time
print("")
time.sleep(1)
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
print_slow("GOOD LUCK!")

#-----------------------------------------------------------------------------------------------------------------------------------------------



def main () : 
    import time
    import math
    
    answer = input("press (Y)")
    if answer == "y" or answer == "Y":
            time.sleep(1)                    #prints line by line
            print("lets play")
            answer = input("press (Y) again to start:").upper()
    if answer == "Y":
            time.sleep(1)
            print("We hope you do better this time" ) 
            start = time.time()
 #----------------------------------------------------------------------------------------------------------------------------------------------  
   
    answer = input ("You have left the jobcentre but you have your first difficult choice of many, do you go left or right ?")
    if answer == "left" or answer == "l": #first left
               
        answer = input ("you decided to turn left on to Cross Lane and walk towards the juntion, it takes a couple of minutes, its in that moment you realise this will be a long journey, which direction will you go? left or right?")
             
        if answer == "left" or answer == "l":
            time.sleep(1)
            print("A homeless man asks you for some change, you give him what little you have and for your kindness he tells you that your heading in the wrong direction")
            time.sleep(1)
            print("He asks you a quick maths question")
            
            answer = input("What is the square root of thirty six?")
            if answer == "six" or answer == "6":
                print("six is correct")
                time.sleep(1)
                
                print("You are now on your way heading in the right direction!")
                answer = input ("Would you now keep going straight or turn left?:")
                if answer == "straight" or answer == "straight":
                    time.sleep(1)
                    print("You just know you are near to your destination, you can feel it, a random stranger stops you and asks if you know an aswer to his crossword puzzle")
                    answer = input ('In the English language, What is the first number to contain the letter "a"?:') 
                    
                    if answer == 'one thousand' or answer == ("1000"): 
                        print('That is correct, one thousand is the first numerical as a word to contain the letter "a"' )
                        time.sleep(1)
                        print("Grateful for you help with the crossword, the stranger offers you help with your directions")
                        time.sleep(1)
                        print("He advises that you keep going straight until you reach 19 Spring Gardens")
                        time.sleep(1)
                        print("You have arrived at:")
                        time.sleep(1)
                        print("             ------                                                                                                                                         ------           ")
                        time.sleep(1)
                        print("          ----                         ||                     ||                                                  |||    -:-                                    ----         ")
                        time.sleep(1)
                        print("        ---'         --------.      - -||- -         -------. ||      -------.  ||    ------        -------. || --|||-¬  |||      ------.     ||    ------        '---       ")
                        time.sleep(1)
                        print("      ----.        -..      |||  -..   ||   ..-   -..      ..-||   ///________| |||..-     -..   ..-       ..|| --|||--  |||   ..'       '..  |||'..     '..       .----     ")
                        time.sleep(1)
                        print("____-----|        |||           |||          ||| |||         |||  ------------| |||-        ||| |||         |||   |||    |||  |||         ||| |||-        |||      |-----____")
                        time.sleep(1)
                        print("¬¬¬¬¬¬¬¬ |        |||           |||          ||| |||         |||  |||           |||-        ||| |||         |||   |||    |||  |||         ||| |||-        |||      |¬¬¬¬¬¬¬¬¬")
                        time.sleep(1)
                        print("     ----.         -..  _ _ |||  -..   _ _  ..-  -..  _ _   ..||  ---  _ _  ..  |||-        |||  ... _ _ _ ..||   ||| _  |||   -..  _ _  ..-  |||-        |||      '----     ")
                        time.sleep(1)
                        print("      ----'.          ------           ---            ---     ||     -------    |||-        |||    .. ------'||   '-___| |||        ---       |||-        |||     .----      ")
                        time.sleep(1)
                        print("        ----                                                                                                                                                    ----         ")
                        print("           ----__                                                                                                                                           __----           ")
                    else:
                        print("That", (answer) ,"is not correct you were late for your appointment")
                    main()
                #---------------------------------------------------------------------------------------------gamelost
                
                
                
                elif answer == "left" or answer == "Left":
                    print("You see a gang of youtes up to no good, they spot you and give chase!!")
                answer = input ("Do you run left or right?")
                
                if answer == "right":
                    time.sleep(1)
                    print("Phew!! You escaped!! that was a close one")
                    time.sleep(1)
                    print("After running for the sake of your health you decide to stop for a drink at a bar, the bar tender says the drink is free if you answer correctly")

                    country_list = [
                        "A):Italy",
                        "B):Spain",
                        "C):Mexico",
                        "D):Cuba",
                    ]
                        print('The Mojito is a traditional rum cocktail from which country?:')

                        choices = (country_list)
                        time.sleep(1)
                        print(*choices, sep = "\n")

                        answer = input()
                    
                        if answer == "cuba" or answer == "d":
                            time.sleep(1)
                        print("Correct, You can see your future it is far now, a young student approaches you and tells you she is conducting a survey to find out how many people are good at maths..")
                        time.sleep(2)
                        print("Hesitant about your own maths skills you agree.. student asks you..")
                        answer = int(input('What is fifthteen percent of two thousand?:'))
                        if answer == 300:
                            time.sleep
                            print("Congratulations that is the correct answer, and have reached your destination!!")
                            time.sleep(1)
                            print("             ------                                                                                                                                         ------           ")
                            time.sleep(1)
                            print("          ----                         ||                     ||                                                  |||    -:-                                    ----         ")
                            time.sleep(1)
                            print("        ---'         --------.      - -||- -         -------. ||      -------.  ||    ------        -------. || --|||-¬  |||      ------.     ||    ------        '---       ")
                            time.sleep(1)
                            print("      ----.        -..      |||  -..   ||   ..-   -..      ..-||   ///________| |||..-     -..   ..-       ..|| --|||--  |||   ..'       '..  |||'..     '..       .----     ")
                            time.sleep(1)
                            print("____-----|        |||           |||          ||| |||         |||  ------------| |||-        ||| |||         |||   |||    |||  |||         ||| |||-        |||      |-----____")
                            time.sleep(1)
                            print("¬¬¬¬¬¬¬¬ |        |||           |||          ||| |||         |||  |||           |||-        ||| |||         |||   |||    |||  |||         ||| |||-        |||      |¬¬¬¬¬¬¬¬¬")
                            time.sleep(1)
                            print("     ----.         -..  _ _ |||  -..   _ _  ..-  -..  _ _   ..||  ---  _ _  ..  |||-        |||  ... _ _ _ ..||   ||| _  |||   -..  _ _  ..-  |||-        |||      '----     ")
                            time.sleep(1)
                            print("      ----'.          ------           ---            ---     ||     -------    |||-        |||    .. ------'||   '-___| |||        ---       |||-        |||     .----      ")
                            time.sleep(1)
                            print("        ----                                                                                                                                                    ----         ")
                            print("           ----__                                                                                                                                           __----           ")
                        else:
                            time.sleep
                            print("That answer is not correct, you wasted to much time and missed your appointment!")
                        main()
                        
                        
                        
                        
                        
                            
                    else:
                        print(answer, "is not correct! you pay £5 for your drink, you get intoxicated beyond belief and miss your appointment")
                    main()
                
                
                
                
                
                
                elif answer == "left":
                    time.sleep(1)
                    print("You were caught and beaten within inches of your life!")
                main()
            #---------------------------------------------------------------------------ends game
            
            
            
            
            else:
                print(answer, ("is incorrect!!"))
            main()
            #----------------------------------------------------------------------------ends game
################################################################################################################RIGHTSIDEPATH            
    elif answer == "right" or answer == "r":  #first right
                answer = input ("")#question
               
 
    elif answer == "right" or answer == "r": #first right
           time.sleep(1)
           print("A citizen has stopped you in the street")
           answer = input ("")
#------------------------------------------------------------------------------------------------------------------------------------------------
           answer = input("left right or straight")
    if answer == "left" or answer == "l": #2nd left
        answer = input ("")
#---------------------------------------------------------------------------------------------------------------------------------------------
        answer = input("left right or straight")
        if answer == "left" or answer == "l":
            answer = input ("")
            answer = input("right or straight")
            if answer == "right" or answer == "r":
                answer = input ("")
            
            elif answer == "straight" or answer == "s":
                time.sleep(1)
                print("You see a gang of youtes up to no good, they spot you and give chase!!")
                answer = input ("Do you run left or right?")
                
                if answer == "right" or answer == "r":
                    time.sleep(1)
                    print("Phew!! You escaped!! that was a close one")
                    answer = input ("")
                
                else:
                    time.sleep(1)
                    print("You were caught and beaten within inches of your life!")
            
    elif answer == "straight" or answer == "s":
        answer = input("left or right")
            
        if answer == "left" or answer == "l":
                print()
        answer = input ("")
        
        if answer == "right":
            time.sleep(1)
            print("Looks like you took the wrong turn")
           
        
        
        
        
        else:
             time.sleep(1)
        print("Looks like you took the wrong turn")
        
    elif answer == "straight" or answer == "s":
        answer = input ("")
        time.sleep(1)
        print("You missed the turn completely, but a citizen kindly pointed you in the right direction")
        answer = input("left right or straight")
        if answer == "left" or answer == "l":
            answer = input ("")
#-------------------------------------------------------------------------------------------------------------------------
    else:
        time.sleep(1)
        print("Looks like you took the wrong turn")
        end = time.time()
        temp = end-start
        hours = temp//3600
        temp = temp - 3600*hours
        minutes = temp//60
        seconds = temp - 60*minutes
        time.sleep(1)
        print('Elapsed time is: %d hrs: %d mins: %d secs' %(hours,minutes,seconds))
        time.sleep(1)
        answer = input("Do you wish to play again?(yes/no)") .lower()
        if answer == "yes" or answer == "y":
            main ()
        else:
            exit ()
main ()
    





