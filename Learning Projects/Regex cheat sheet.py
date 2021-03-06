"""Some regex syntax and functions that I'm likely to forget, so I'm writing them down here in a cheat sheet"""

#more in-depth explanations found here: https://developers.google.com/edu/python/regular-expressions

#an actual cheat-sheet available here: https://www.debuggex.com/cheatsheet/regex/python

#metacharacters and special sequences:
# '.' = wildcard
# '^' = start of a string
# '$' = end of a string
# '*' means 0 or more repetitions (in case of optional, but positional, repetition)
# '+' = 1 or more repetitions
# '?' = 0 or 1 repetitions
# '|' = or (as in (this|that) == 'this' or 'that')
# '{x,y}' = range of repetitions (for instance, r'birds{1,5}' would be between 1 and 5 instances of the word 'birds')
# '[]' = create a set of characters to check from (use '[aeiou]' to check if a word contains any vowels)
# '[^]' = check for anything *not* contained in that set (re.search([^0-9]) to make sure a string contains something other than digits)
# '?P<name>' = named group - works like dictionaries (match.group('name'))
# '?:...' = non-capturing group (doesn't affect group indices, or show up in group())
# r'(.+)\1' = special sequence that looks for one repetition of a repeating wildcard
# '\d', '\s', '\w' = digits, whitespace, word characters (unicode) - uppercase means 'not' (e.g. '\D' means 'not a digit')
# '\A' = start of a string, '\Z' = end of a string, and '\b' represents a word barrier, between words in a string



import re

my_string = 'This is how I check my regex functions!'

#Use 'match' to see if a string starts with something
if re.match('This', my_string):
  print("Starts with 'This'")
if not re.match('The other', my_string):
  print("Does not start with 'The Other'")

#use 'Search' to check if a string contains something
if re.search('how', my_string):
  print("String contains the word 'how'")
if not re.search('bazinga', my_string):
  print("String does not contain the word 'bazinga'. Obviously")

#print every instance of something in a string
print(re.findall('is', my_string))

#find where something occurs within a string
match = re.search('check', my_string)
if match:
  print(match.start())
  print(match.end())
  print(match.span())
  
  
#change things within a string
new_string = re.sub('test', 'check', my_string)
print(new_string)


#return instances of a match with group() or groups()
letters = r'i(s)'
match1 = re.search(letters, my_string)
if match1:
  print(match1.group())
  print(match1.group(1))
  print(match1.groups())
  print(match1.groups(1))
  
