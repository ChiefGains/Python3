#!user/bin/env Python3

"""This is a useless program that prints things to a certain number of prints as defined by the user"""

from time import sleep

#this dictionary key pair tells the function which loop it should be using
key = {'l': 'yes'}

def print_things(x):
    while key['l'] == 'yes':
        for i in range(10):
            print(f'Print job #{i+1}')
            sleep(1)
            #normally I love list comprehension, but afaik I can't use the sleep() function that way
            if i == (x-1):
                key['l'] = 'no'
                #change the dictionary key, thus breaking the loop

    while key['l'] == 'no':
        print('This function is over!')
        break
        #we only want it to print once, so we break to ensure it doesn't go forever
