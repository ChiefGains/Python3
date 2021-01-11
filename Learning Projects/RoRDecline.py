def calc(x, y, z):
    #x is inital RoR, y is ror decline per minute, z is length of roast
    total = x

    i = 0

    while i < z:
        x -= y
        total += x
        i+= 1
    
    print(total)

calc(20, 2, 10)
calc(18, 1.5, 11)