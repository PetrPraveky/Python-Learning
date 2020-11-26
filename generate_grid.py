import random

# Funkce pro zadávaní hodnot a přípravu přížky
def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("musí být >=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)

#User input mřížky
rows = get_int("řádků:", 1, None)
columns = get_int("sloupců:", 1, None)
minimum = get_int("minimum (nebo Enter pro 0): ", -1000000, 0)

default = 1000
if default < minimum:
    default = 2 * minimum
maximum = get_int("maximum (nebo Enter pro "+ str(default) +"): ", minimum, default)

#Vypsání mřížky
row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) < 10:
            s = " " + s
        line += s
        column += 1
    print(line)
    row += 1