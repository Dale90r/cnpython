import time

    
    


time.sleep(1)
print("ooooooooooooo                                              o      oooooo                    o8                oooooo                                           ")        
time.sleep(1)
print("8'   888   `8                                           .d88    d8P'  `Y8b                  888             d8P'  `Y8b                                         ")       
time.sleep(0.5)
print("     888       .ooooo.   .oooo.   ooo. .oo.  .oo.     .d'888   888           .ooooo.   .oooo888   .ooooo.  888            .oooo.   ooo. .oo.  .oo.    .ooooo.  ")  
time.sleep(0.5)   
print("     888      d88' `88b `P  )88b  `888P Y88bP Y88b  .d'  888   888          d88' `88b d88' `888  d88' `88b 888           `P  )88b  `888P Y88bP Y88b  d88' `88b ") 
time.sleep(0.5)     
print("     888      888ooo888  .oP 888   888   888   888  88ooo888oo 888          888   888 888   888  888ooo888 888     ooooo  .oP 888   888   888   888  888ooo888 ") 
time.sleep(0.5)    
print("     888      888    .o d8(  888   888   888   888       888   `88b    ooo  888   888 888   888  888    .o `88.    .88'  d8(  888   888   888   888  888    .o ") 
time.sleep(0.5)    
print("    o888o     Y8bod8P' `Y888  8o o888o o888o o888o     o888o   `Y8bood8P'  `Y8bod8P' `Y8bod88P   Y8bod8P    Y8bood8P    `Y888 8o o888o o888o o888o `Y8bod8P    ")



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
print ("The rules of the game are as follows: Arrive at CodeNation in the quickest time possible")
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


    


answer = input("press (Y) to play")

#-----------------------------------------------------------------------------------------------------------------------------------------------

if answer == "y" or answer == "Y":
    time.sleep(1)                    #prints line by line
print("lets play")
answer = input("press (Y) again to start:").upper()
if answer == "y" or "Y":
    time.sleep(1)
print("You can do it") 
start = time.time()

   
    
time.sleep(0.5)
print("=========================================================================================")
time.sleep(0.5)
print("===============  =======================================================  ===============")
time.sleep(0.5)
print("===============  =======================================================  ===============")
time.sleep(0.5)
print("===============  ===========================  ==========================  ===============")
time.sleep(0.5)
print("====  ===   ===  ======   ====   ===  = ===    ==  =   ====   ===    ===  ==  =  ===   ==")
time.sleep(0.5)
print("========     ==    ===  =  ==  =  ==     ===  ===    =  ==  =  ==  =  ==  ==  =  ==  =  =")
time.sleep(0.5)
print("====  ==  =  ==  =  ==  =====     ==  =  ===  ===  =======     ==  =  ==  ==  =  ===  ===")
time.sleep(0.5)
print("====  ==  =  ==  =  ==  =====  =====  =  ===  ===  =======  =====    ===  ==  =  ====  ==")
time.sleep(0.5)
print("=  =  ==  =  ==  =  ==  =  ==  =  ==  =  ===  ===  =======  =  ==  =====  ==  =  ==  =  =")
time.sleep(0.5)
print("==   ====   ===    ====   ====   ===  =  ===   ==  ========   ===  =====  ===    ===   ==")
time.sleep(0.5)
print("=========================================================================================")
###########################################################-------------------------------------------------------------------------------------------------

answer = input ("You have left the jobcentre but you have your first difficult choice of many, do you go left or right ?")
if answer == "left" or answer == "l":
    answer = input ("you decided to turn left on to Cross Lane and walk towards the juntion, it takes a couple of minutes, its in that moment you realise this will be a long journey, which direction will you go? left or right?")
    if answer == "right" or answer == "r":
        print("You encounter a homeless man who asks if you can spare some change, you give him what little you have and he tells you that your heading in the right direction")
        time.sleep(1)
        print("There is another man at a bus stop, he asks you to help him with a quick maths problem...")
        answer = input ("What is the square root of 36?")
        if answer == "six" or answer == "6":
            answer = input(" He thanks you, as you head down the street you arrive at a junction do you continue straight or go left?:")
            if answer == "straight":
                time.sleep(1)
                print("You just know you are near to your destination, you can feel it, a random stranger stops you and asks if you know an aswer to his crossword puzzle")
                answer = input ('In the English language, What is the first number to contain the letter "a"?:') 
                
                if answer == 'one thousand' or answer == ("1000"):
                    time.sleep(1)
                    print("You see a large group of protesters and you think to yourself...")
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
                        print("Quadrillion is correctY")
                    elif answer == "Quadrillion" or answer == "quadrillion":
                        print(answer, ("is correct!"))
                    elif answer == "QUADRILLION":
                        print(answer, ("is correct!"))
                        time.sleep(1)
                        print("You manage to get through the crowd on time for your appointment!!")
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
                        print(answer, ("Is not correct, it takes to long to get through the crowd, you arrive late to your appointment!"))

                
                else:
                    print("You thought there was something wrong with this guy and he becomes furious when you answer incorrectly, you dont make your appointment!")



            elif answer == "left":
                time.sleep(1)
                print("You see a gang of youts up to no good..Oh no they have spotted you!!")
                time.sleep(0.1)
                print("You are now in trouble, they are chasing you!!")
                time.sleep(1)
                answer = input ("Will you run left or right?:")
                if answer == "right":
                    time.sleep(0.5)
                    print("Pheww! that was close but you escaped!")
                    time.sleep(1)
                    print("After running for the good of your own health you go into a bar for a drink, the bartender says the drink is free if you can answer his question!")
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
                        answer = input ("The student asks.. what is fiftheen percent of two thousand? hesitantly you answer..")
                        if answer == "300" or "three hundred":
                            time.sleep(1)
                            print("Answer Correct!, you can see your destination! .. You have made it!")
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
                            time.sleep(1)
                            print("Unfortunatley she decides to keep asking you more questions as she finds you amusing, you miss your appointment!")
                            print("@@@@@@@   @@@@@@  @@@@@@@@@@  @@@@@@@@ ")
                            time.sleep(0.5)
                            print(" !@@       @@!  @@@ @@! @@! @@! @@!    ") 
                            time.sleep(0.5) 
                            print(" !@! @!@!@ @!@!@!@! @!! !!@ @!@ @!!!:! ")
                            time.sleep(0.5)  
                            print(" :!!   !!: !!:  !!! !!:     !!: !!:    ")    
                            time.sleep(0.5)
                            print(" :: :: :   :   : :  :      :   : :: :::")
                            time.sleep(0.5)
                            print("  @@@@@@  @@@  @@@ @@@@@@@@ @@@@@@@    ")
                            time.sleep(0.5)
                            print(" @@!  @@@ @@!  @@@ @@!      @@!  @@@   ")
                            time.sleep(0.5)
                            print(" @!@  !@! @!@  !@! @!!!:!   @!@!!@!    ")
                            time.sleep(0.5)
                            print(" !!:  !!!  !: .:!  !!:      !!: :!!    ")
                            time.sleep(0.5)
                            print("  : :. :     ::    : :: :::  :   : :   ")






                    else:
                        print("You have taken to long in the bar and are now drunk beyond belief! and missed your appointment!")   
                elif answer == "left":
                    time.sleep(0.1)
                    print("You have been caught!!, they beat you within inches of your life and cannot attend your appointment!")
                    time.sleep(1)
                    print("@@@@@@@   @@@@@@  @@@@@@@@@@  @@@@@@@@ ")
                    time.sleep(0.5)
                    print(" !@@       @@!  @@@ @@! @@! @@! @@!    ") 
                    time.sleep(0.5) 
                    print(" !@! @!@!@ @!@!@!@! @!! !!@ @!@ @!!!:! ")
                    time.sleep(0.5)  
                    print(" :!!   !!: !!:  !!! !!:     !!: !!:    ")    
                    time.sleep(0.5)
                    print(" :: :: :   :   : :  :      :   : :: :::")
                    time.sleep(0.5)
                    print("  @@@@@@  @@@  @@@ @@@@@@@@ @@@@@@@    ")
                    time.sleep(0.5)
                    print(" @@!  @@@ @@!  @@@ @@!      @@!  @@@   ")
                    time.sleep(0.5)
                    print(" @!@  !@! @!@  !@! @!!!:!   @!@!!@!    ")
                    time.sleep(0.5)
                    print(" !!:  !!!  !: .:!  !!:      !!: :!!    ")
                    time.sleep(0.5)
                    print("  : :. :     ::    : :: :::  :   : :   ")



    else:
        print("Ooops, you took a wrong turn!!")
        time.sleep(0.5)
        print("@@@@@@@   @@@@@@  @@@@@@@@@@  @@@@@@@@ ")
        time.sleep(0.5)
        print(" !@@       @@!  @@@ @@! @@! @@! @@!    ") 
        time.sleep(0.5) 
        print(" !@! @!@!@ @!@!@!@! @!! !!@ @!@ @!!!:! ")
        time.sleep(0.5)  
        print(" :!!   !!: !!:  !!! !!:     !!: !!:    ")    
        time.sleep(0.5)
        print(" :: :: :   :   : :  :      :   : :: :::")
        time.sleep(0.5)
                                                
        print("  @@@@@@  @@@  @@@ @@@@@@@@ @@@@@@@    ")
        time.sleep(0.5)
        print(" @@!  @@@ @@!  @@@ @@!      @@!  @@@   ")
        time.sleep(0.5)
        print(" @!@  !@! @!@  !@! @!!!:!   @!@!!@!    ")
        time.sleep(0.5)
        print(" !!:  !!!  !: .:!  !!:      !!: :!!    ")
        time.sleep(0.5)
        print("  : :. :     ::    : :: :::  :   : :   ")


                
######################################################--------------------------------------------------------------------------------



elif answer == "right":
    answer = input ("you decided to turn right and walk towards the juntion, it takes a couple of minutes, its in that moment you realise this will be a long journey, which direction will you go? left or right or straight ahead?")
    if answer == "left":
        answer = input("you are traveling down a long road, do you want to keep goin straight or to turn right?")
        if answer == "straight":
            answer = input("Still on the same very long road, only this time you have the option of left or right, which will you choose?")
            if answer == "left":
                print("A strange man approches you, he asks you a question that seems very random..how do you respond?")
                print("He asks you, which country does the Faroe islands belong to?")
                options_list = [
                    'A):Denmark',
                    'B):Sweden',
                    'C):Russia',
                    'D):I dont know, leave me alone'
                    ]
                answer = options_list
                input()
                if answer == "A" or answer == "Denmark":
                    print("That is the correct answer")
                    print("Because you answered the strange mans question he directed you to a shortcut to get to Codenation, it was closer than you thought!!")
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
                elif answer == "B"or answer =="C":
                    print("No way your talking rubbish!!")
                else:
                    print("the strange man pulls out a knif and chances you, you never make it to your appointment!")
                    time.sleep(0.5)
                    print("@@@@@@@   @@@@@@  @@@@@@@@@@  @@@@@@@@ ")
                    time.sleep(0.5)
                    print(" !@@       @@!  @@@ @@! @@! @@! @@!    ") 
                    time.sleep(0.5) 
                    print(" !@! @!@!@ @!@!@!@! @!! !!@ @!@ @!!!:! ")
                    time.sleep(0.5)  
                    print(" :!!   !!: !!:  !!! !!:     !!: !!:    ")    
                    time.sleep(0.5)
                    print(" :: :: :   :   : :  :      :   : :: :::")
                    time.sleep(0.5)
                                                            
                    print("  @@@@@@  @@@  @@@ @@@@@@@@ @@@@@@@    ")
                    time.sleep(0.5)
                    print(" @@!  @@@ @@!  @@@ @@!      @@!  @@@   ")
                    time.sleep(0.5)
                    print(" @!@  !@! @!@  !@! @!!!:!   @!@!!@!    ")
                    time.sleep(0.5)
                    print(" !!:  !!!  !: .:!  !!:      !!: :!!    ")
                    time.sleep(0.5)
                    print("  : :. :     ::    : :: :::  :   : :   ")

            elif answer == "right":
                print("You were mugged")
        



        elif answer == "right":
            print(" You were hit by a speeding motorist...")
        time.sleep(0.5)
        print("@@@@@@@   @@@@@@  @@@@@@@@@@  @@@@@@@@ ")
        time.sleep(0.5)
        print(" !@@       @@!  @@@ @@! @@! @@! @@!    ") 
        time.sleep(0.5) 
        print(" !@! @!@!@ @!@!@!@! @!! !!@ @!@ @!!!:! ")
        time.sleep(0.5)  
        print(" :!!   !!: !!:  !!! !!:     !!: !!:    ")    
        time.sleep(0.5)
        print(" :: :: :   :   : :  :      :   : :: :::")
        time.sleep(0.5)
                                                
        print("  @@@@@@  @@@  @@@ @@@@@@@@ @@@@@@@    ")
        time.sleep(0.5)
        print(" @@!  @@@ @@!  @@@ @@!      @@!  @@@   ")
        time.sleep(0.5)
        print(" @!@  !@! @!@  !@! @!!!:!   @!@!!@!    ")
        time.sleep(0.5)
        print(" !!:  !!!  !: .:!  !!:      !!: :!!    ")
        time.sleep(0.5)
        print("  : :. :     ::    : :: :::  :   : :   ")

    if answer =="straight":
        print("you have encountered an old lady doing a crossword puzzle..")
        answer = input ("She asks you what the name of the ring UFC fighters fight in?")
        if answer == "the octagon" or answer == "octagon":
            print(answer, "is the right answer!") 
        elif answer == "Octagon" or answer == "Octagon":
            print(answer, "No, no, no, thats the name of the ring UFC fighters fight in")
        else:
            print(answer, "is incorrect!!")
#############--------------------------------------------------------------------------------------------------------------------------------
        
    end = time.time()
    temp = end-start
    hours = temp//3600
    temp = temp - 3600*hours
    minutes = temp//60
    seconds = temp - 60*minutes
    time.sleep(1)
    print('Elapsed time is: %d hrs: %d mins: %d secs' %(hours,minutes,seconds))
  
    
       
