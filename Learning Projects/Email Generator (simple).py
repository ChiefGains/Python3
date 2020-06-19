"""Very simple version of a program that will take input and automatically
  generate an email for you. Useful for things like subscriber lists,
  automated thank-yous, or newsletters (if paired with a database)"""
  
import pyperclip
from random import randint as choice

#to help give the illusion of sincerity, we'll give ourselves a list of signatures to choose from
signatures = ['Sincerely', 'Forever yours', 'In deepest love', 'Yeah... anyways...']

def choose_email(type, index = choice(0, len(signatures)-1)):
    signature = signatures[index]
    if type == "thank_you":
        recipient = input('Enter name of recipient')
        kindness = input('What are you thanking this person for?')
        spouse = input('What is your spouse\'s name?')
        name = input('What is your name?')

        pyperclip.copy(f"{recipient},\n\n    Thank you so much for the"\
                 f" {kindness}, it was truly a blessing to both {spouse} "\
                 f"and myself.\n\n{signature},\n\n {name}")

    elif type == "newsletter":
        recipient = input('Enter name of recipient')
        newsletter = input('What is the name of the newsletter?')
        name = input('What is your name?')
        company = input('What is the name of your company?')

        pyperclip.copy(f"{name},\n\n    Thank you for making the choice to "\
                       f"subscribe to {newsletter}! You will definitely, "\
                       f"totally, certainly NOT regret this choice. Probably."\
                       f"\n\n{signature}, {name}, CEO of {company}.")

    else:
        print("That type of email does not exist")


choose_email("thank_you", 2)

print(pyperclip.paste())

choose_email("newsletter")

print(pyperclip.paste())
                       
