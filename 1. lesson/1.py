#Program na vypsání úloh s číslami
print("Zadávej postupně čísla a pro přerušení a vypsání výsledku zade Enter:")
#Základní proměné
total = 0
count = 0
low = 9 #Musí být 9 pro případ, že by bylo nejmenší číslo např 8
high = 0 #Musí být 0 pro případ, že by bylo největší číslo např 0
#Vyhodnocení zadaného výrazu a provedení operací
while True:
    line = input("Zadej celá čísla: ") #Zadání
    if line:
        try:
            number = int(line) #Otestuje, zda-li je zadání číslo
        except ValueError as err:
            print(err) #Není-li to číslo, vypíše error a opakuje
            continue
        if number >= high: #Otestuje, zda-li je číslo nejvetší, pokud-li ne, přeskočí to
            high = number
        if number <= low: #Otestuje, zda-li je číslo nejmenší, pokud-li ne, přeskočí to
            low = number
        total += number #Přičtení čísla k celkové hodnotě
        count += 1 #Počet zadaných čísel
    else:
        break
#Vypsání promených
if count:
    print("počet= ", count, "celkem= ", total, "nejmenší= ", low, "největší= ", high, "průměr= ", total/count)