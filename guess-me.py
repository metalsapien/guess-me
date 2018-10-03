
########################################
########################################
######     Guessing Challenge     ######
########################################
######   Author: Harsh Nath Jha   ######
########################################
########################################

import random
answer = random.randint(1,100)
list = []
print('\n##############################\n####  Guessing Challenge  ####\n##############################')
print("\nI'm thinking of a number between 1 to 100, what is it?\n")

while True:
    
    guess = 0
    while guess not in range(1,101):
        guess = int(input('Your guess? (1-100): '))
    list.append(guess)

    if len(list) == 1 and list[0] != answer:
        if abs(list[-1] - answer) <= 10:
            print('WARM')
        else:
            print('COLD')
            
    elif len(list) == 1 and list[0] == answer:
        print('\nToo lucky! You guessed right in your FIRST attempt!')
        break
            
    else:
        if list[-1] == answer:
            print('\nAwesome, you guessed it right in {} attempts!'.format(len(list)))
            break
        elif (abs(list[-1] - answer) < abs(list[-2] - answer)):
            print('WARMER')
        else:
            print('COLDER')