def main () : 
    import time
    
    answer = input("press (Y)")
    if answer == "yes" or "y":

        time.sleep(1)                    
        print("lets play")
    answer = input("press (Y) again to start:").upper()
    if answer == "Y" or answer == "yes":
            time.sleep(1)
            print("We hope you do better this time" ) 
    start = time.time()
#-------------------------------------------------------------
    end = time.time()
    temp = end-start
    hours = temp // 3600
    temp = temp - 3600*hours
    minutes = temp//60
    seconds = temp - 60*minutes
    print('Elapsed time is: %d hrs: %d mins: %d secs' %(hours,minutes,seconds))
    
    answer = input("Do you wish to play again?(yes/no)") .lower()
    if answer == "yes" or answer == "y":
            main ()
    else:
            exit ()
main ()