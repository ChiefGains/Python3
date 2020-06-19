#!user/bin/env Python3

#random program for simulating dice roll

from random import randint as rand

def roll_dice(x, y):
  roll = [rand(1,y) for i in range(x)]
  print(roll)
  
#for this function, input how many dice you would like to roll, and it will return a list of randomly generated integers,
#where x is equal to the number of dice thrown, and y is equal to the number of sides for each die. In this implementation,
#all dice must have the same number of sides
