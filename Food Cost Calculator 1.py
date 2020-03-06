"""These are the beginnings of a food cost calculator.
    this program allows you to create menu items, then
    feed those items into a recipe, which returns cost"""


#Version 0.1
#This program currently sucks hardcore.In its current state, it is
#less efficient then just manually doing this in Excel. Eventually
#it will utilize Excel spreadsheets to store ingredient info, and
#allow users to create n number of recipes based off of ingredients



class Ingredient():
    def __init__(self, name, cost, unit, amount):
        self.name = name
        self.cost = cost
        self.unit = unit
        self.amount = amount
        self.unit_cost = self.cost/self.amount
        self.check_unit_cost()

        
    def check_unit_cost(self):
        print('Unit cost of ', self.name, ' is:\n', '$', round(self.unit_cost, 2), ' per ', self.unit, sep='')



class Recipe():
    def __init__(self, *args, servings = 1):
        self.cost = 0
        self.servings = servings
        

        for arg in args:
            amt = int(input(f'How much {arg.name} does this recipe use?'))
            self.cost += amt*arg.unit_cost
            
        self.serving_cost = self.cost/self.servings
        
        print('The cost of this recipe is:\n$', self.cost, sep='')
        print('The cost per serving is:\n$', self.serving_cost, sep='')

water = Ingredient('water', 10, 'oz', 128)

salt = Ingredient('salt', 5, 'g', 200)

water_recipe = Recipe(water, salt, servings = 2)
