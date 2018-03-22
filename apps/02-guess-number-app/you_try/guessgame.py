#!/usb/bin/env python
# a simple guessing game

import random

print('_' *50)
print('              Guessing game!  ')
print('_' *50)
print()
print('guess a number between 1 and 100\n')
randNumber = random.randint(1, 100)
found = False

name = input('please tell me your name\n')
while not found:
    guess_text = int(input('Enter your guess:\n'))
    if guess_text == randNumber:
        print('you got it! {0}, the correct number was {1}'.format(name, randNumber))
        found = True
    elif guess_text > randNumber:
        print('guess lower')
    else:
        print('guess higher')




