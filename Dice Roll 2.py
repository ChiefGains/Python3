#!user/bin/env Python3

"""Another dice roller, but more convoluted! This one accepts user input.
    ***However*** - this one does NOT allow the user to choose how many sides the dice have"""

#as always, the first thing we do is import our modules

from random import randint as roll
from time import sleep


def roll_dice():
  #We'll take user input here to see how many dice to roll
    x = input('How many dice would you like to roll?')
    try:
        #Input always returns a string value, so we'll first check to make sure that the string
        #is in face a number, then we'll convert it to an integer for later use
        x.isnumeric()
        y = int(x)
        if y > 10:
            print("Sorry, that's too many dice. Enter a number less than 10")
            sleep(2)
            roll_dice()
        elif y <= 0:
            print('How about try a positive number there, chief')
            sleep(2)
            roll_dice()
        else:
            print('You rolled:')
            for i in range(y):
                print(roll(1,6), end = " ")
            #this loop allows us to put that user input to good use,
            #and using end = " " ensures that the numbers all print on the same line
    except:
        raise
        print("Let's try entering a number, smart-alec")
        sleep(2)
        roll_dice()
