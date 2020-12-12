#Program na vykreslení exponenciální funkce
#Funkce uživatelského vstupu
def user_input(msg, minimum, maximum, default):
    while True:
        try:
            x = input(msg) #Uživatelský vstup
            if x == '': #Otestování, zda-li uživatel nezadal nic
                x = default #Přiřazení záklandí hodnoty
                break
            else:
                x = int(x) #Dosazení x za číslo (kvůli chybám)
                if x > maximum: #Otestování, zda-li zadané číslo není vetší jak maximum
                    x = maximum #Přiřazení maximální hodnoty
                    break
                elif x < minimum: #Otestování, zda-li zadané číslo není menší jak minimum
                    x = minimum #Přiřazení minimální hodnoty
                    break
                else:
                    break
        except ValueError as err: #Chybová hláška
            print(err) #Vypsání chybové hlášky
            continue
    return x #Výstup x hodnoty
#Funkce vykreslení exponeciální křivky
def func_graf(max_cycle, maximum, space):
    print("\n\n\n") #Oddělení textu
    max_cycle_str = str(max_cycle) #Změna hodnoty vstupu z int na str
    box_headline = "GRAF EXPONENCIÁLNÍ FUNKCE S POČETEM OPERACÍ: "+max_cycle_str #Nadpis listu
    box_space_left, box_space_right, box_space_up, box_space_down = space*2, space*2, space, space #Odstazení stran listu
    a, b, c, d, e = 0, 0, 0, 0, 2 #Proměné na opakovací funkce
    ex_num, ex_num_max = 1, 1 #Exponenciální čísla
    while a < max_cycle: #Funkce na výpočet exponenciálního čísla
        ex_num = ex_num*2 #Výpočet exponenciálního číslo
        a += 1 #Odstranění "nekonečného" řetězce
    while b < maximum: #funkce na výpočet maximálního exponenciálního čísla
        ex_num_max = ex_num_max*2 #Výpočet maximálního exponenciálního čísla
        b += 1 #Odstranění "nekonečného" řetězce
    ex_g_heigh, ex_g_width = ex_num, 1 #Imanigární délka křídel funkce
    ex_num_heigh, ex_num_width = ex_num, ex_num/2 #Numerická délka křídel funkce
    ex_g_lenght = ex_num+max_cycle #Výška funkce od 0
    ex_g_max_lenght = ex_num_max*2+max_cycle-4 #Šířka funkce od 0
    space_left, space_right = ex_g_max_lenght, 0 #Odsazení od grafu od kraje listu a od y-osy
    offset_y = (ex_num_max+max_cycle-1)-(ex_num+max_cycle)+2 #Přesah y-osy
    line, v_line =  0, ex_g_lenght+offset_y-2 #Počet řádků
    line_num = ["0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]
                #List pro čísla na y-ose
    box_updown_side = ex_g_max_lenght+box_space_left+box_space_right+2+2+box_space_right #Délka horní a dolní strany listu
    box_headline_center = int((box_updown_side/2)-(len(box_headline)/2)) #Hodnota pro vycentrování nadpisu listu
    box_headline_side_test = int(box_headline_center*2+(len(box_headline))) #Hodnota pro test vycentrování nadpisu listu
    print("┌"+(box_updown_side)*"—"+"┐") #Vykresléní horní hranice listu
    box_headline = "GRAF EXPONENCIÁLNÍ FUNKCE S POČETEM OPERACÍ: "+max_cycle_str #Nadpis listu
    if int(box_headline_side_test) < box_updown_side: #Otestovaní, zda-li hodnota vycentrování je nebo není celé číslo
        print("|"+int(box_headline_center+1)*" "+box_headline+(box_headline_center*" ")+"|") #Úprava vypsání u druhé možnosti
    else:
        print("|"+(box_headline_center*" ")+box_headline+(box_headline_center*" ")+"|") #Vypsání u první možnosti
    print("┝"+(box_updown_side)*"—"+"┤") #Vykreslení dolní hranice boxu nadpisu
    while d < box_space_up: #Funkce na odsazení grafu od nadpisu
        print("|"+(box_updown_side)*" "+"|") #Vykreslení části hran listu
        d += 1 #Odstranění "nekonečného" řetězce
    while c < offset_y: #Funkce vykreslení přesahu y-osy
        print("|"+box_space_left*" "+(+space_left+1)*" "+"│"+box_space_right*" "+(line_num[v_line])+box_space_right*" "+"|") #Vykreslení přesahu y-osy
        c += 1 #Odstranění "nekonečného" řetězce
        v_line -= 1 #Odpočet řádků u popisu osy
    while ex_num_heigh > 1: #Funkce na vykreslení horního ramena grafu
        ex_g_heigh = ex_g_heigh/2 #Zmenšování vykreslovací výšky ramena grafu
        while line < ex_g_heigh: #Funkce vykreslení "rovných" částí ramena
            print(("|"+box_space_left*" "+space_left*" "+"#"+space_right*" "+"|"+box_space_right*" "+(line_num[v_line])+box_space_right*" "+"|")) #Vykreslení "rovné" části grafu
            line += 1 #Odstranení "nekonečného" řetězce
            v_line -= 1 #Odpočet řádků u popisu osy
        line = 0 #Vyresetování opakovací hodnoty
        space_left -= 1 #Odsazení rovné části od osy
        ex_num_heigh /= 2 #Zmenšení zbývající výšky ramena
        space_right += 1 #Odsazení rovné části od osy
    space_left += 1 #Odstranění duplikovaného bodu
    space_right -= 2 #odstranění duplikovaného bodu
    while ex_num_width > 1: #Funkce na vykreslení spodního ramena grafu
        ex_g_width = ex_g_width*2 #Zvetšování vykreslovací šířky ramena grafu
        space_left -= ex_g_width*2 #Kalibrace odsazení od strany listu
        space_right += ex_g_width #Kalibrace odsazení od osy
        line = 0 #Kontrolní vyresetování opakovací hodnoty
        while line < 1: #Funkce vykreslení "rovných" částí ramena
            print(("|"+box_space_left*" "+space_left*" "+ex_g_width*"# "+space_right*" "+"|"+box_space_right*" "+(line_num[v_line])+box_space_right*" "+"|")) #Vykreslení "rovné" části grafu
            line += 1 #Odstranění "nekonečného" řetězce
            v_line -= 1 #Odpočet řádků u popisu osy
        line = 0 #Vyresetování opakovací hodnoty
        ex_num_width /= 2 #Zmenšení zbývající šířky ramena
    offset_x = (ex_num_max*2)+max_cycle-3 #Přesah x-osy
    print("|"+box_space_left*" "+offset_x*"—"+"╇"+(box_space_right-5)*"—"+5*" "+(line_num[v_line])+box_space_right*" "+"|") #Vykreslení spodní části listu se záporným přesahem z-osy
    while e < box_space_down: #Funkce záporného prodloužení y-osy 
        print("|"+box_space_left*" "+offset_x*" "+"|"+(box_space_right*2+2)*" "+"|") #Vykreslení záporného prodloužení y-osy
        e += 1 #Odstranění "nekonečného" řetězce
    e = 2 #Vyresetování opakovací proměné
    while e < box_space_down: #Funkce odsazení spodní hranice listu od grafu
        print("|"+(box_space_left+offset_x+(box_space_right*2)+2+1)*" "+"|") #Vykreslení odsazení spodní hranice listu od grafu 
        e += 1 #Odstranění "nekonečného" řetězce
    print("└"+(box_updown_side)*"—"+"┘") #Vykreslení spodní hranice grafu
#Halvní funkce, kterou voláme
def main():
    minimum, maximum, default = 1, 5, 3 #Maximální, minimální a základní hodnota grafu
    print("Zadej číslo, které bude představovat délku procesu zobrazení exponenciání funkce.\n"
          "Číslo bude převážně představovat počet řádku vykreslení, tudíž má nějaké hranice.\n"
          "   [Minimální hodnota: ",minimum," | Maximální hodnota: ",maximum," | Základní hodnota: ",default,"]\n")
          #Výpis instrukcí
    x = user_input("Zadej číslo: ", minimum, maximum, default) #Uživatelský vstup
    func_graf(x, maximum, 8) #Vykreslení grafu
#Volání hlavní funkce
main()