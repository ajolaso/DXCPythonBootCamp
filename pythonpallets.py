print("Welcome to ATM Bank")
restart = ('Y')
balance = 1000.00
chances = 3

while chances >= 0:
    pin = int(input('\nPlease enter your PIN'))
    if pin == (1234):
        print('Pin Verified!\n')
        while restart not in ('n', 'NO', 'no', 'N'):
            print('*******MENU********')
            print('Please Type 1 to check your balance')
            print('Please Type 2 to quit')
            option = int(input('What would you like to do?'))
            if option == 1:
                print('Your balance is ' + str(balance))
                restart = input('Would you like to go back?')
                if restart in ('n', 'NO', 'no', 'N'):
                    break
            elif option == 2:
                print('Thank you')
                break
            else:
                print('Please enter the correct pin')
                restart()
    elif pin != (1234):
        print('Incorrect Pin')
        chances = chances - 1
        if chances == 0:
            print('no more attempts')
            break