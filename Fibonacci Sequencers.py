#We'll give ourselves two different ways to sequence fibonacci numbers: to a number of places, or to a max number


#First, we'll make a function that sequences fibonacci to a max number of places

def fib_places(x):
    i = 0
    y = [0, 1]
    while len(y) < x:
        y.append(y[i]+y[i+1])
        i += 1

    return y    

#Now we'll do it again, but this time we'll ask for a maximum value instead of number of places

def fib_max(x):
    i = 0
    y = [0, 1]
    while max(y) < x:
        y.append(y[i]+y[i+1])
        i += 1

    return y[:-1]
    
#you may have noticed that this calculates one *higher* than the max number entered. My solution was to simply not print the final
#index in list y, but I'm sure there are more elegant and pythonic ways to accomplish this
