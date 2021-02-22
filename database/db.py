#Program databáze
#Vložení modulů
import os #Vložení modulu operačního systému
import json #Vložení modulu .JSON souborů
filename = "./data.json" #Přidání souboru databáze
#Seznam slov/argumentů
argum = ["NEW", "OPEN", "DATA", "END", "BACK", "EDIT", "NAME", "SURNAME", "BDATE", "NICK", "REMOVE", "WARN", "Y", "N", "SEX"]
nu_arg_List = ["Jméno", "Příjmení", "Datum narození (DD/MM/YYYY)", "Přezdívku", "Rodné číslo", "Pohlaví (M/F)"]
monts = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
days = ["31", "29", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
sexargs = ["M", "F"]
#Funkce vyčištění konzole
def cmd_clear():
    os.system('cls') #Vyčistí konzoli
#Funkce kontroly platnosti datumu
def date_check(msg):
    while True: #Cyklus True
        try:
            x = input(msg) #Uživatelský vstup
            dates = x.split("/") #Rozdělí strin datumu ve formátu DD/MM/RRRR na list [DD, MM, RRRR]
            #Testuje správnost datumu bez února
            if dates[0] <= days[int(dates[1])-1] and dates[1] in monts and dates[1] != monts[1] and int(dates[2]) < 10000:
                break
            #Testuje správnost přestupního roku
            elif dates[1] == monts[1] and int(dates[2])%4 == 0 and dates[0] <= days[1]:
                break
            elif dates[1] == monts[1] and int(dates[2])%4 != 0 and dates[0] < days[1]:
                break
            else: #Vypsání chyby zadání špatného datumu
                continue
        except IndexError:
            print("'"+x+"'"+" Není správné datum")
            continue
    return x #Vrátí původní datum
#Funkce na kontrolu a vyplnění rodného čísla
def bnum_check(msg, date, sex):
    dates = date.split("/")
    if sex == "M":
        count = 0
    elif sex == "F":
        count = 50
    month = int(dates[1])+count
    if month < 10:
        month = "0"+str(month)
    else:
        month = str(month)
    while True:
        try:
            y = input(msg+" "+dates[2][2:]+month+dates[0]+"/")
            test = int(y)
            if int(y) < 1000:
                test = int("s")
            elif int(y) > 9999:
                test = int("s")
            bnum = dates[2][2:]+month+dates[0]+y
            if int(bnum)%11 != 0:
                test = int("s")
            break
        except ValueError:
            print("Špatně zadané číslo, pokud-li chcete pokračovat [Y], pokud-li chcete skončit [N]")
            while True:
                x = input(msg)
                if x in argum:
                    if x == argum[12]:
                        argument = 0
                        break
                    elif x == argum[13]:
                        argument = 1
                        break
                else:
                    continue
            if argument != 1:
                    continue
            else:
                bnum = "null"
                break     
    return bnum
#Soubor funkcí textu a databáze
def databaze(part, mem):
    #Funkce hlavního textu
    def opening():
        number = 0
        cmd_clear() #Vyčištění konzole
        print('\033[1m'+"Toto je program databáze, postupujte dle pokynů...") #Vypsání textu
        print('\033[0m') #Vypsání textu
        with open (filename, "r") as f:
            temp = json.load(f)
            for entry in temp:
                if entry["bnum"] == "null":
                    number += 1
        if number > 0:
            print("!!! U "+str(number)+" uživatelů nemáte zadané rodné číslo [WARN] pro otevření.\n")
        print("   Přeje te si přidat nového člena [NEW]?\n   Otevřít již zadaného [OPEN]? \n   Nebo otevřít databázy [DATA]?\n   Ukončit program [END]?\n") #Vypsání textu
        
        user_input(0, " >: ", number) #Zavolání funkce uživatelského vstupu na hlaní straně
    #Funkce zadání nového člena
    def new_user():
        cmd_clear() #Vyčištění konzole
        print("\033[1m"+"\nZadávání nového uživatele..."+"\033[0m") #Vypsání textu
        print("Postupujte dle instrukcí:\n") #Vypsání textu
        user_input(1, " >: ", nu_arg_List) #Zavolání funkce uživatelského vstupu pro zadání nového uživatele
    #Funkce otevření databáze členů
    def open_data():
        cmd_clear() #Vyčištění konzole
        print("\033[1m"+"\nNačítání databáze uživatelů..."+"\033[0m") #Vypsání textu
        print("\033[1m"+"ID"+" "*6+"Jméno"+10*" "+"Příjmení"+10*" "+"Pohlaví"+" "*2+"Datum narození"+9*" "+"Rodné číslo"+" "*9+"Přezdívka"+10*" "+"\033[0m") #Vypsání textu
        with open (filename, "r") as f: #Otevření a načtení JSON databáze
            temp = json.load(f) #Uložení listu databáze do promněnné 
            for entry in temp: #Pro proměnou v listu databáze
                name = entry["name"] #Založení promněnné "name" z databáze
                surname = entry["surname"] #Založení promněnné "surname" z databáze
                bdate = entry["bdate"] #Založení promněnné "bdate" z databáze
                nick = entry["nick"] #Založení promněnné "nick" z databáze
                ident = entry["ID"] #Založení promněnné "ident" z databáze
                sex = entry["sex"]
                bnum = entry["bnum"]
                if bnum == "null":
                    bnum = " "
                    num = 1
                else:
                    num = len(bnum)
                #Vypsání listu uživatelů
                print("0"*(3-len(str(ident)))+str(ident)+" "*5+name+" "*(15-len(name))+surname+" "*(18-len(surname))+sex+" "*8+bdate+" "*(23-len(bdate))+bnum+" "*(20-num)+nick+" "*(19-len(nick)))
            while True: #Cyklus True
                print("\n Zadat dalšího uživotale? [NEW]\n Zpět na počáteční výběr? [BACK]\n Ukončit? [END]") #Vypsnání textu
                x = input(" >: ") #Uživatelský vstup
                if x in argum: #Test, zda-li je x v listu argumentů
                    if x == argum[0]: #Pokud-li je x rovno NEW
                        databaze("NEWUSER", 0) #Zavolá funkci vytvoření nového uživatele
                        break #Zlomí cyklus
                    elif x == argum[4]: #Zda-li je x rovno BACK
                        databaze("OPENING", 0) #Zavolá funcki hlavní nabídky
                        break #Zlomí cyklus
                    elif x == argum[3]: #Zda-li je x rovno END
                        cmd_clear() #Vyčistí konzoli
                        print("\033[1m"+"\nUkončování..."+"\033[0m") #Vypsání textu
                        break #Zlomí cyklus
                else: #Když x není v listu:
                    continue #Opakuje cyklus
                break
    #Funcke otevření uživatele
    def open_user():
        cmd_clear() #vyčištění konzole
        print("\033[1m"+"\nNačítání existujícího uživatele..."+"\033[0m") #Vypsání textu
        print("Zadejte ID uživatele:") #Vypsnání textu
        user_input(2, " >: ", nu_arg_List) #Zavolání funkce uživatelského vstupu pro otevření uživatele
    #Funkce pro úpravu otevřeného uživatele
    def edit_user(mem): 
        print("\033[1m"+"\nÚprava uřivatele..."+"\033[0m") #Vypsnání text
        user_input(3, " >: ", mem) #Zavolání funkce uživatelského vstupu pro úpravu uživatele
    #Soubor pro určení správné funkce
    if part == "OPENING": #Určení správné funkce
        opening() #Vyvolání funkce
    elif part == "NEWUSER": #Určení správné funce
        new_user() #Vyvolání funkce
    elif part == "OPENDATA": #Určení správné funce
        open_data() #Vyvolání funkce
    elif part == "OPENUSER": #Určení správné funce
        open_user() #Vyvolání funkce
    elif part == "EDITUSER": #Určení správné funce
        edit_user(mem) #vyvolání funkce
#Soubor funkcí uživatelského vstupu
def user_input(part, msg, lst):
    #Funkce uživatelského vstupu na hlavní straně
    def mainpage_input(msg, lst):
        while True: #Cyklus
            x = input(msg) #Uživatelský vstup
            if x in argum: #Otestuje, zda-li je proměnná "x" v seznamu
                if x == argum[0]: #První položka seznamu
                    databaze("NEWUSER", 0) #Zavolá funkci pro nového uživatele
                    break #Zlomení cyklu
                elif x == argum[1]: #Druhá položka seznamu
                    databaze("OPENUSER", 0) #Zavolá funkci pro otevření databáze
                    break #Zlomení cyklu
                elif x == argum[2]: #Třetí položka seznamu
                    databaze("OPENDATA", 0)
                    break #Zlomení cyklu
                elif x == argum[3]: #Čtvrtá položka seznamu
                    cmd_clear() #Vyčištění konzole
                    print("\033[1m"+"\nUkončování..."+"\033[0m") #Vypsání textu
                    break #Zlomení cyklu
            else: #Pokud-li proměnná "x" v seznamu není
                continue #Opakuje cyklus
    #Funkce vytvoření nového uživatele
    def newuser_input(msg, lst):
        data = {} #List data
        ident = 0 #Promněnná ID
        while True: #Cyklus True
            with open (filename, "r") as f: #Otevření a načtení JSON databáze
                temp = json.load(f) #Uložení listu databáze do promněnné 
            print("Zadejte: "+lst[0]) #Vypsání textu
            data["name"] = input(msg) #Zložení jména do listu data
            print("Zadejte: "+lst[1]) #Vypsání textu
            data["surname"] = input(msg) #Založení příjmení do listu data
            print("Zadejte: "+nu_arg_List[2])
            bdate = date_check(msg) #Zavolání funkce na kontrolu datumu
            data["bdate"] = bdate #Založení datumu do listu data
            print("Zadejte: "+lst[3]) #Vypsnání textu
            data["nick"] = input(msg) #Založení pžezdívky do listu data
            print("Zadejte: "+lst[5])
            while True:
                sex = input(msg)
                if sex.upper() in sexargs:
                    break
                else:
                    print("Zadané "+sex+" není správný formát")
                    continue
            data["sex"] = sex
            print("Chcete zadat"+lst[4]+" [Y/N]")
            while True:
                x = input(msg)
                if x in argum:
                    if x == argum[12]:
                        bnum = bnum_check(msg, bdate, sex)
                        break
                    elif x == argum[13]:
                        bnum = "null"
                        break
                    else:
                        continue
            data["bnum"] = bnum
            for keyval in temp: #Pro proměnou v listu databáze
                while True: #Cyklus True
                    if ident == keyval['ID']: #Cyklus nalezení nejvyššího ID
                        ident += 1 #Přidání +1 k nejvyššímu ID
                        continue #Opakování
                    else: #Pokud-li je nejvyšší ID nalezeno
                        break #Zlomit cyklus
            data["ID"] = ident #Založení ID do listu data
            temp.append(data) #Přidání listu data na konec listu temp
            with open (filename, "w") as f: #Otevření a načtení JSON databáze
                json.dump(temp, f, indent=7) #Zapsnání nové části databáze
            while True: #Cyklus true
                print("\n Zadat dalšího uživatele? [NEW]\n Zpět na počáteční výběr? [BACK]\n Ukončit? [END]") #Vypsání textu
                x = input(msg) #Uživatelský vstup
                if x in argum: #test, zda-li je x v listu argumentů
                    if x == argum[0]: #Pokud-li je x rovno NEW
                        databaze("NEWUSER", 0) #Zavolá funkci nového uživatele
                        break #Zlomit cyklus
                    elif x == argum[4]: #Pokud-li je x rovno BACK
                        databaze("OPENING", 0) #Zavolá funkci hlavní nabídky
                        break #Zlomit cyklus
                    elif x == argum[3]: #Pokud-li je x rovno END
                        cmd_clear() #vyčištění konzole
                        print("\033[1m"+"\nUkončování..."+"\033[0m") #Vypsání textu
                        break #Zlomit cysklus
            break #Zlomit cyklus
    #Funkce otevření uživatele
    def open_user_input(msg, lst):
        with open (filename, "r") as f:
            temp = json.load(f)
            while True:
                x = input(msg)
                for entry in temp:
                    if str(x) == str(entry['ID']):
                        name = entry['name']
                        surname = entry['surname']
                        bdate = entry['bdate']
                        nick = entry['nick']
                        sex = entry["sex"]
                        bnum = entry["bnum"]
                        if bnum == "null":
                            bnum = " "
                            num = 1
                        else:
                            num = len(bnum)
                        print("\033[1m"+"Jméno"+10*" "+"Příjmení"+10*" "+"Pohlaví"+" "*2+"Datum narození"+9*" "+"Rodné číslo"+" "*9+"Přezdívka"+10*" "+"\033[0m")
                        print(name+" "*(15-len(name))+surname+" "*(18-len(surname))+sex+" "*8+bdate+" "*(23-len(bdate))+bnum+" "*(20-num)+nick+" "*(19-len(nick)))
                        while True:
                            print("\n Upravit uživatele? [EDIT]\n Zadat dalšího uživatele? [NEW]\n Zpět na počáteční výběr? [BACK]\n Ukončit? [END]")
                            y = input(msg)
                            if y in argum:
                                if y == argum[0]:
                                    databaze("NEWUSER", 0)
                                    break
                                elif y == argum[4]:
                                    databaze("OPENING", 0)
                                    break
                                elif y == argum[3]:
                                    print("\033[1m"+"\nUkončování..."+"\033[0m")
                                    break
                                elif y == argum[5]:
                                    databaze("EDITUSER", x)
                                    break
                        break
                    else:
                        continue
                

    def edit_user_input(msg, lst):
        while True:
            print("Chce upravit: "+"\033[1m"+"Jméno "+"\033[0m"+"- [NAME]")
            print(" "*14+"\033[1m"+"Příjmení "+"\033[0m"+"- [SURNAME]")
            print(" "*14+"\033[1m"+"Pohlaví "+"\033[0m"+"- [SEX]")
            print(" "*14+"\033[1m"+"Datum narození "+"\033[0m"+"- [BDATE]")
            print(" "*14+"\033[1m"+"Přezdívku "+"\033[0m"+"- [NICK]")
            print(" "*14+"\033[1m"+"Nebo smazat uživatele "+"\033[0m"+"- [REMOVE]")
            with open (filename, "r") as f:
                temp = json.load(f)
                f.close()
                for entry in temp:
                    if str(lst) == str(entry['ID']):
                        name = entry['name']
                        surname = entry['surname']
                        bdate = entry['bdate']
                        nick = entry['nick']
                        sex = entry["sex"]
                        bnum = entry["bnum"]
                        ident = entry["ID"]
                        while True:
                            x = input(msg)
                            if x in argum:
                                if x == argum[6]:
                                    y = input("\n >: Napište nové jméno: ")
                                    print(' Nové jméno je: '+y)
                                    entry.clear()
                                    name = y
                                    break
                                if x == argum[7]:
                                    y = input("\n >: Napište nové příjmení: ")
                                    print(' Nové příjmení je: '+y)
                                    entry.clear()
                                    surname = y
                                    break
                                if x == argum[8]:
                                    y = date_check("\n >: Napište nové datum narození (DD/MM/RRRR): ")
                                    print(' Nové datum narození je: '+y)
                                    print(' Vytvoření nového rodného čísla: ')
                                    z = bnum_check(" >: ", y, sex)
                                    print(' Nové rodné číslo je: '+z)
                                    entry.clear()
                                    bdate = y
                                    bnum = z
                                    break
                                if x == argum[9]:
                                    y = input("\n >: Napište novou přezdívku: ")
                                    print(' Nová přezdívka je: '+y)
                                    entry.clear()
                                    entry = y
                                    break
                                if x == argum[14]:
                                    y = input("\n >: Napište jiné pohlaví: ")
                                    while True:
                                        if y == "F" or y == "M":
                                            if y == sex:
                                                sex = sex
                                                print(" Vaše pohlaví se nezměnilo")
                                                break
                                            elif y != sex:
                                                sex = y
                                                print(' Změněné pohlaví je: '+sex)
                                                print(' Vytvoření nového rodného čísla: ')
                                                z = bnum_check(" >: ", bdate, sex)
                                                print(' Nové rodné číslo je: '+z)
                                                bnum = z
                                                break
                                        else:
                                            print('Špatně zadané pohlaví...')
                                            continue
                                    break
                                else:
                                    print("Nesprávně zadaný argument")
                                    continue
                        entry['name'] = name
                        entry['surname'] = surname
                        entry['bdate'] = bdate
                        entry['nick'] = nick
                        entry['sex'] = sex
                        entry['bnum'] = bnum
                        entry['ID'] = ident
                        with open (filename, "w") as f: #Otevření a načtení JSON databáze
                            json.dump(temp, f)
                        break
                while True:
                    print("\n Nadále upravovat uživatele? [EDIT]\n Zadat dalšího uživatele? [NEW]\n Zpět na počáteční výběr? [BACK]\n Ukončit? [END]") #Vypsání textu
                    x = input(msg) #Uživatelský vstup
                    if x in argum: #test, zda-li je x v listu argumentů
                        if x == argum[0]: #Pokud-li je x rovno NEW
                            databaze("NEWUSER", 0) #Zavolá funkci nového uživatele
                            break #Zlomit cyklus
                        elif x == argum[4]: #Pokud-li je x rovno BACK
                            databaze("OPENING", 0) #Zavolá funkci hlavní nabídky
                            break #Zlomit cyklus
                        elif x == argum[3]: #Pokud-li je x rovno END
                            cmd_clear() #vyčištění konzole
                            print("\033[1m"+"\nUkončování..."+"\033[0m") #Vypsání textu
                            break
                        elif x == argum[5]:
                            databaze("EDITUSER", lst)
                            break
                break

    if part == 0: #Určení správné funkce
        mainpage_input(msg, lst) #Volání funkce
    elif part == 1:
        newuser_input(msg, lst)
    elif part == 2:
        open_user_input(msg, lst)
    elif part == 3:
        edit_user_input(msg, lst)

#Halvní funkce
def main():
    databaze("OPENING", 0)
main()