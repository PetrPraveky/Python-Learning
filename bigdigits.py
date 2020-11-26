import sys

#BIG DIGITS
zero = [" ***  ", "*   * ", "*   * ", "*   * ", " ***  "] #0
one = ["  *   ", " **   ", "  *   ", "  *   ", " ***  "] #1
two = [" ***  ", "*   * ", "   *  ", "  *   ", "***** "] #2
three = [" ***  ", "*   * ", "  **  ", "*   * ", " ***  "] #3
four = ["   *  ", "  **  ", " * *  ", "***** ", "   *  "] #4
five = [" ***  ", "*     ", " **   ", "   *  ", "***   "] #5
six = [" ***  ", "*     ", " ***  ", "*   * ", " ***  "] #6
seven = ["***** ", "   *  ", "   *  ", "  *   ", "  *   "] #7
eight = [" ***  ", "*   * ", " ***  ", "*   * ", " ***  "] #8
nine = [" ***  ", "*   * ", " **** ", "    * ", "    * "] #9

Digits = [zero, one, two, three, four, five, six, seven, eight, nine]

try:
    digits = sys.argv[1] #Napsaný text v konzoli
    row = 0
    while row < 7:
        line = "" #Vytisknutý text v konzoli
        column = 0 #Počet opakování (zanků)
        while column < len(digits): #Zda-li není počet opakování většé nebo roven délce Importovaného textu
            number = int(digits[column]) #Vybrání správného čísla na správné pozici
            digit = Digits[number] #Vybrání správného číslo z BIG DIGITS
            line += digit[row] #Přidíní čísla do textu
            column += 1 #Přidání počtu opakování
        print(line)
        row += 1
except IndexError:
    print("použití: bigdigits.py <číslo>")
except ValueError as err:
    print(err, "v", digits)

