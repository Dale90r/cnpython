


def dispense_cash(entered_pin, requested_amount, balance):
    pin = 1234
    balance = 300

    
    if entered_pin == pin and requested_amount < balance:
        print('Pin is correct, requested amount {} balance is {}'.format(requested_amount, balance))
    
               
    else:
        requested_amount > balance
        print("insufficient funds or incorrect pin")
    

dispense_cash(1235, 20, 300)
