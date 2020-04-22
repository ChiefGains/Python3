import re
import os
import importlib
from random import randint as rand


def play():
    while True:
        choice = input('Would you like to play a mad lib? 1 = yes')
        if choice == '1':
            libs = [x for x in os.listdir('libs')]
            friendly_lib = ', '.join(libs)
            choice2 = input('1 for random, 2 to choose')
            if choice2 == '1':
                lib = libs[rand(0, len(libs)-1)]
                run_lib(lib)
            elif choice2 == '2':
                print('Which madlib would you like to play?')
                lib = input(friendly_lib)
                if lib in libs:
                    run_lib(lib)
                else:
                    print('That choice is not available')
            else:
                print("I didn't get that")
        else:
            quit()

	

def run_lib(lib):

    madlib_text = ['libs', lib]

    text_path = '\\'.join(madlib_text)

    with open(text_path, 'r') as t:
        text=t.read()
        prompts = re.findall('\[(.*?)\]', text)
        answers = []
        for prompt in prompts:
            if re.match(r'[^aeiou]', prompt):
                x = input(f'Please enter a {prompt}')
            else:
                x= input(f'Please enter an {prompt}')
            answers.append(x)

        i = 0

        while i < len(answers):
            text = text.replace(prompts[i], answers[i], 1)

            i += 1

        print(text)
        

play()
