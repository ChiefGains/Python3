#separate words by iterating through and checking for white space

words = input('Enter words separated by spaces, human\n')

i = 0

wordlist = []

print(len(words))

print(len(words) - 1)

while i < len(words) - 1: #The loop doesn't break when the condition is met
    #therefore the backup below. Stupid python
    letters = []
    while words[i] != ' ':
        letters.append(words[i])
        i += 1
        if i == len(words):
            break
    word = ''.join(letters)
    wordlist.append(word)
    i += 1

print(wordlist)