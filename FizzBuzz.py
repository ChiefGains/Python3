from random import randint as rand

n = rand(0,100)

for i in range(n):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)