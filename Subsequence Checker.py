#Checks to see if a string is a subsequence of another string

def checkSub(string1, string2):
    print(f'Checking to see if {string2} is a subsequence of {string1}')
    subsequence = []
    i = 0
    j = 0
    while j < len(string2):
        #print(f'i = {i}, j = {j}')
        if i == len(string1):
            break
        elif string2[j] == string1[i]:
            print(f'{string2[j]} found!')
            subsequence.append(string2[j])
            i += 1
            j += 1
        else:
            i += 1
    
    if ''.join(subsequence) == string2:
        print(f'Congrats! {string2} is a subsequence of {string1}!')
    else:
        print(f'Sorry, {string2} is not a subsequence of {string1}')


string = 'I wish I were an Oscar Meyer Weiner'

myList = ['Moth', 'candy', 'wan', 'won', 'wOn' 'basil']



for word in myList:
    checkSub(string, word)
    