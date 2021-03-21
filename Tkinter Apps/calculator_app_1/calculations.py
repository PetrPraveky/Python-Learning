import json
import os
#Třída kalkulac
number_new = ""
def calc_connected():
    print("     calculations.py")

class OpenFile():
    #Otevření "data.json" a "locale" souborů
    global locale_file, data, locale, locale_default #Registrování proměnných
    with open("./data.json", "r") as g: #Otevření dat
        data = json.load(g) #Načtení dat
        g.close() #Zavření původního souboru
    #Otevření souborů jazka
    locale_file = "locale/"+data["locale"] #Přidání správné cesty k lokalizacím
    with open(locale_file, "r", encoding="UTF-8") as f: #Otevření lkkalizace
        locale = json.load(f) #Načtení lokalizace
        f.close() #Zavření původního souboru
        locale_default = 0
    

class BasicCalculator():
    def BC_calculations(self, oper, number):
        return