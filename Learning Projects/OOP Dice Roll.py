#!user/bin/env Python3

#This time we're rolling dice using OOP! What fun! How convoluted!

#it's a dice roller, so of course we need randint
from random import randint as rand


class Die:
    def __init__(self, sides):
        self.sides = sides

    #if we don't enter an argument, the die will roll once when this method is called
    def roll(self, x = 1):
        return [rand(1, self.sides) for i in range(x)]

#we'll make a couple dice to play with
six = Die(6)
fourteen = Die(14)


def roll_two(a, b):
    x = int(input("How many times would you like to roll?"))
    #the zip function lets us see the lists as concurrent rolls
    return list(zip(a.roll(x),b.roll(x)))
