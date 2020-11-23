#Program na generaci náhodného textu
import random
#Proměné
pronoun = ["můj", "tvůj", "jeho", "její", "jejich"] #Zájmena
noun = ["kočka", "pes", "muž", "žena", "chalec", "dívka"] #Podstatné jméno
verb = ["zpívá", "brečí", "skáče", "běží", "říká", "chodí"] #Sloveso
adverb = ["hlasitě", "tiše", "hrozně", "krásně", "kvalitně"] #Příslovce
x = 0 #Proměná hotových cyklů
y = 0 #Počet řádků
default = 5 #Základní počet řádků
maximum = 10 #Maximální počet řádků
minimum = 1 #Minimální počet řádků
#User input počtu řádků
while True:
    try:
        y = input("Zadej počet řádků: ") #zadání řádku
        if y == '': #Pokud-li se zadá Enter, automaticky to doplní hodnotu default
            y = default
            break
        else:
            y = int(y) #Přepsání y hodnoty na int
            if y > maximum: #Pokud-li zadaná hodnota překročí maximum, automaticky se sníží na maximální hodnotu
                y = 10
                break
            elif y < minimum: #Pokud-li zadaná hodnota překročí minimum, automaticky se sníží na minimální hodnotu
                y = 1
                break
            else:
                break
    except ValueError as err: #Vypsání erroru při zadání špatné hodnoty typu str
        print(err)
        continue
#Generace náhodného textu
while x < y: #Opakování do té doby, než se počet hotových cyklu bude rovnat počtu zadaných řádků
    i = random.randint(0,1) #Náhodný výběr mezi větou delší a kratší
    if i == 0:
        sentence = random.choice(pronoun)+" "+random.choice(noun)+" "+random.choice(adverb)+" "+random.choice(verb) #Náhodná generace delší věty
        print(sentence) #Vypsání věty
        x += 1 #Přidání 1 k počtu hotových cyklů
        continue
    elif i == 1:
        sentence = random.choice(pronoun)+" "+random.choice(noun)+" "+random.choice(verb) #Náhodná generace kratší věty
        print(sentence) #Vypsání věty
        x += 1 #Přidání 1 k počtu hotových cybklů
        continue
    else:
        break