import math
import cmath
from tkinter import *
from tkinter import font 
import json
import os
from types import SimpleNamespace

default = 0
calculator_option = default
#Funkce pro připojení modulu s "kalkulačkou"
import calculations as calc
#Funkce pro vypsání připojených modulů do konzole
def main_connected():
    print("\nmain.py has been connected to file:")
    calc.calc_connected()
    print("\n")

#Třída pro otevření souborů s daty
class OpenFile():
    #Otevření "data.json" a "locale" souborů
    def file_opener(self):
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
    #Vypsání dat v konzili
    file_opener(0) #Zavolání funkce na otveření souboru
    os.system('cls') #Vyčištění konzole
    print(f"DATA: (data.json)\n{data}") #Vypsnání obsahu "data.json"
    print(f"\nLOCALES: ({locale_file})\n{locale}") #Vypsání obsahu "locale"
    mode = data['dark_light_mode'] #Přiřazení správné možnosti pro změnu vzhledu
  
#Třída funkčnosti
class Func(OpenFile):
    global new_locale
    new_locale = data['locale']
    #Funkce zavření okna
    def func_quit(self, root):
        root.destroy()
        
    #Funkce obnovení okna díky oknu možností
    def func_mode_reload(self, root, val):
        self.func_quit(root) #Zavření okna možnosti
        render_main_frame.pack_forget() #"Zapomenutí" hlavního rámu
        self.func_settings_change(val)
        self.render_main(val) #Znovu vytvoření hlavního rámu
        
    #Funkce pro uložení změny vzhledu
    def func_settings_change(self, val):
        with open("./data.json", "r+") as t:
            new_data = json.load(t)
            new_data['dark_light_mode'] = val
            t.seek(0)
            json.dump(new_data, t, indent=4)
            t.truncate()
            t.close()
            
    #Funkce pro uložení jazyka
    def func_locale_save(self):
        with open("./data.json", "r+") as h:
            new_data = json.load(h)
            new_data['locale'] = self.new_locale
            h.seek(0)
            json.dump(new_data, h, indent=4)
            h.truncate()
            h.close()
    
    #Funkce změny vzhledu
    def func_appear_change(self, val):  
        print("\ndakr/light mode has been set to: "+str(val))
        
    #Funkce na změnu jazyka    
    def func_laguage_change(self, root, value):
        print("\nlocalisation file set to: "+value)
        self.new_locale = value
        self.func_locale_save()
        self.func_quit(root)
        render_main_frame.pack_forget()
        self.file_opener()
        self.render_main(data['dark_light_mode'])
        

#Třída renderu
class Render(Func):    
    #Funkce pro vytvoření hlavní stránky
    def render_main(self, mode):
        global render_main_frame
        #Funkce pro barvy
        self.render_dark_light_mode(mode)
        #Vytvoření, které pokrývá celou aplikaci
        render_main_frame = Frame(self.main_root, bg=main_background_color)
        render_main_frame.grid_columnconfigure(0, weight=1)
        render_main_frame.grid_rowconfigure(0, weight=0)
        #Zavolání funkce pro vytvožení horní lišty
        self.render_upper_bar()
        #Vykreslení horní lišty
        render_upper_bar_frame.grid(row = 0, column=0, sticky='ew')
        #Vykreslení celého pole
        if calculator_option == 0:
            self.render_basic_calculator()
            render_bc_frame.grid(row=1, column=0, sticky='w', padx=50, pady=30)
        else:
            pass
        render_main_frame.pack(fill='both', expand="True")
    
    #Funkce pro určení dark/light módem
    def render_dark_light_mode(self, mode):
        global main_background_color, main_text_color, upper_bar_frame_bg_color, upper_bar_frame_bg_color_hover, upper_bar_frame_submenu_color, upper_bar_frame_submenu_color_hover, mode_window_background_color, mode_window_background_color_hover
        global calc_background_color_1, calc_background_color_2, calc_background_color_2_hover
        if mode == 1: #Tmavý režim
            main_background_color = '#1c1c1c' #Barva hlavního pozadí
            #Barva pozadí u nastavení
            mode_window_background_color = '#242424' #Barva pozadí okna změny vzhledu
            mode_window_background_color_hover = '#424242' #Aktivní barva pozadí okna změny vzhledu
            #Barva textu
            main_text_color = '#f5f5f5' #Barva textu
            #Horní lišta
            upper_bar_frame_bg_color = '#242424' #Barva pozadí
            upper_bar_frame_bg_color_hover = '#424242' #Barva pozadí, když je na něm myš
            upper_bar_frame_submenu_color = "#595959" #Barva podmenu
            upper_bar_frame_submenu_color_hover = '#808080' #Barva podmenu, když je na něm myš
            #Kalkulačka
            calc_background_color_1 = '#242424'
            calc_background_color_2 = '#424242'
            calc_background_color_2_hover = '#595959'
            
        elif mode == 0: #Světlý režim
            main_background_color = '#f5f5f5' #Barva hlavního pozadí
            mode_window_background_color = '#d1d1d1' #Barva pozadí okna změny vzhledu
            mode_window_background_color_hover = 'b3b3b3' #Aktivní barva pozadí okna změny vzhledu
            #Barva textu
            main_text_color = '#0d0d0d' #Barva textu
            #Horní lišta
            upper_bar_frame_bg_color = '#d1d1d1' #Barva pozadí
            upper_bar_frame_bg_color_hover = '#b3b3b3' #Barva pozadí, když je na něm myš
            upper_bar_frame_submenu_color = "#e0e0e0" #Barva podmenu
            upper_bar_frame_submenu_color_hover = '#cccccc' #Barva podmenu, když je na něm myš
            #Kalkulačka
            calc_background_color_1 = '#d1d1d1'
            calc_background_color_2 = '#b3b3b3'
            calc_background_color_2_hover = '#e0e0e0'
            
        else: #Custom
            main_background_color = '#0d0d0d'
    
    #Funkce pro vykreslení základní kalkulačky
    def render_basic_calculator(self):
        global render_bc_frame
        #Vytovření rámu pro základkní kalkulačku
        render_bc_frame = Frame(render_main_frame, bg=calc_background_color_1, relief='sunken', borderwidth="2", padx=4, pady=4)
        #Titulek
        render_bc_title = Label(render_bc_frame, bg=calc_background_color_1, font='bold', fg=main_text_color, text=locale['BC_title'])
        render_bc_title.grid(row=1, column=0, padx=5, pady=5, columnspan=5)
        #Vytvoření vstupu
        render_bc_input_box = Entry(render_bc_frame, width=25, relief='sunken', bg=calc_background_color_2, fg=main_text_color, justify='right', font='bold')
        render_bc_input_box.grid(row=2, column=0, padx=5, pady=5, columnspan=5)
        #Vytvoření tlačítek
        #0_0 == řádek 0 a sloupec 0
        #Řádek 1
        render_bc_button_1_0 = Button(render_bc_frame, padx=9, pady=6, text="x²", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_1_1 = Button(render_bc_frame, padx=11.5, pady=6, text="(", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_1_2 = Button(render_bc_frame, padx=11.5, pady=6, text=")", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_1_3 = Button(render_bc_frame, padx=10.3, pady=6, text="×", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_1_4 = Button(render_bc_frame, padx=11.2, pady=6, text="/", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        #Řádek 2
        render_bc_button_2_0 = Button(render_bc_frame, padx=10.2, pady=6, text="√", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_2_1 = Button(render_bc_frame, padx=11, pady=6, text="7", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_2_2 = Button(render_bc_frame, padx=11, pady=6, text="8", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_2_3 = Button(render_bc_frame, padx=11, pady=6, text="9", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_2_4 = Button(render_bc_frame, padx=11, pady=6, text="-", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        #Řádek 3
        render_bc_button_3_0 = Button(render_bc_frame, padx=11, pady=6, text="↑", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_3_1 = Button(render_bc_frame, padx=11, pady=6, text="4", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_3_2 = Button(render_bc_frame, padx=11, pady=6, text="5", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_3_3 = Button(render_bc_frame, padx=11, pady=6, text="6", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_3_4 = Button(render_bc_frame, padx=10, pady=6, text="+", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        #Řádek 4
        render_bc_button_4_0 = Button(render_bc_frame, padx=11, pady=6, text="0", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_4_1 = Button(render_bc_frame, padx=11, pady=6, text="1", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_4_2 = Button(render_bc_frame, padx=11, pady=6, text="2", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_4_3 = Button(render_bc_frame, padx=11, pady=6, text="3", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        render_bc_button_4_4 = Button(render_bc_frame, padx=10, pady=6, text="=", fg=main_text_color, bg=calc_background_color_2, activebackground=calc_background_color_2_hover, activeforeground=main_text_color, cursor='hand2')
        #Vykreslení tlačítek
        #Řádek 1
        render_bc_button_1_0.grid(row=3, column=0, sticky='W', padx=5, pady=5)
        render_bc_button_1_1.grid(row=3, column=1, sticky='W', padx=5, pady=5)
        render_bc_button_1_2.grid(row=3, column=2, sticky='W', padx=5, pady=5)
        render_bc_button_1_3.grid(row=3, column=3, sticky='W', padx=5, pady=5)
        render_bc_button_1_4.grid(row=3, column=4, sticky='W', padx=5, pady=5)
        #Řádek
        render_bc_button_2_0.grid(row=4, column=0, sticky='W', padx=5, pady=5)
        render_bc_button_2_1.grid(row=4, column=1, sticky='W', padx=5, pady=5)
        render_bc_button_2_2.grid(row=4, column=2, sticky='W', padx=5, pady=5)
        render_bc_button_2_3.grid(row=4, column=3, sticky='W', padx=5, pady=5)
        render_bc_button_2_4.grid(row=4, column=4, sticky='W', padx=5, pady=5)
        #Řádek 3
        render_bc_button_3_0.grid(row=5, column=0, sticky='W', padx=5, pady=5)
        render_bc_button_3_1.grid(row=5, column=1, sticky='W', padx=5, pady=5)
        render_bc_button_3_2.grid(row=5, column=2, sticky='W', padx=5, pady=5)
        render_bc_button_3_3.grid(row=5, column=3, sticky='W', padx=5, pady=5)
        render_bc_button_3_4.grid(row=5, column=4, sticky='W', padx=5, pady=5)
        #Řádek 4
        render_bc_button_4_0.grid(row=6, column=0, sticky='W', padx=5, pady=5)
        render_bc_button_4_1.grid(row=6, column=1, sticky='W', padx=5, pady=5)
        render_bc_button_4_2.grid(row=6, column=2, sticky='W', padx=5, pady=5)
        render_bc_button_4_3.grid(row=6, column=3, sticky='W', padx=5, pady=5)
        render_bc_button_4_4.grid(row=6, column=4, sticky='W', padx=5, pady=5)
    
    #Funkce pro vytvoření horní lišty
    def render_upper_bar(self):
        global render_upper_bar_frame
        #Vytvoření horní lišty
        render_upper_bar_frame = Frame(render_main_frame, bg=upper_bar_frame_bg_color, relief='raised', borderwidth="2")
        #Vytvoření tlačítek na liště
        render_upper_list_btn = Menubutton(render_upper_bar_frame, text=locale["UB_LB_text"], fg=main_text_color, bg=upper_bar_frame_bg_color, padx=15, activebackground=upper_bar_frame_bg_color_hover, activeforeground=main_text_color, relief='groove', borderwidth="0.5", cursor='hand2')
        render_upper_settings_btn = Menubutton(render_upper_bar_frame, text=locale["UB_SB_text"], fg=main_text_color, bg=upper_bar_frame_bg_color, padx=25, activebackground=upper_bar_frame_bg_color_hover, activeforeground=main_text_color, relief='groove', borderwidth="0.5", cursor='hand2')
        #Vykreslení tlačítek na liště
        render_upper_list_btn.grid(row = 0, column= 0)
        render_upper_settings_btn.grid(row=0, column=1)
        #Vytvoření podlistu pro tlačítka
        render_upper_list_submenu = Menu(render_upper_list_btn, tearoff=0, bg=upper_bar_frame_submenu_color, fg=main_text_color, disabledforeground=main_text_color, cursor='hand2')
        render_upper_settings_submenu = Menu(render_upper_settings_btn, tearoff=0, bg=upper_bar_frame_submenu_color, fg=main_text_color, disabledforeground=main_text_color, cursor='hand2')
        #Přidání položek do podlistu pro 1. tlačítko
        render_upper_list_submenu.add_command(label="×  "+locale['UB_LSM_option_1'], activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color, state='normal')
        render_upper_list_submenu.add_command(label="×  "+locale['UB_LSM_option_2'], activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color, state='disabled')
        render_upper_list_submenu.add_command(label="×  "+locale['UB_LSM_option_3'], activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color, state='disabled')
        render_upper_list_submenu.add_command(label="×  "+locale['UB_LSM_option_4'], activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color, state="disabled")
        render_upper_list_submenu.add_command(label="×  "+locale['UB_LSM_option_5'], activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color, state='disabled')
        render_upper_list_submenu.add_separator()
        render_upper_list_submenu.add_command(label="×  "+locale['UB_LSM_option_6'], activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color, state='normal', command=lambda:self.func_quit(self.main_root))
        #Přidání položek do podlistu pro 2. tlačítko
        render_upper_settings_submenu.add_command(label="×  "+locale['UB_SSM_option_1'], activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color, state='normal', command=self.render_dark_light_mode_window)
        render_upper_settings_submenu.add_command(label="×  "+locale['UB_SSM_option_2'], activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color, state='disabled', command=self.render_locale_type_window)
        #Zpárování podlistů k tlačítkům
        render_upper_settings_btn.config(menu= render_upper_settings_submenu)
        render_upper_list_btn.config(menu= render_upper_list_submenu)

    #Funkce vytvoření nového okna pro změnu vzhledu
    def render_dark_light_mode_window(self):
        #Vytvoření nového okna
        render_mode_window = Toplevel()
        render_mode_window.title(locale["DL_MW_title"])
        render_mode_window.geometry(str(data['light_dark_mode_resolution']))
        render_mode_window.resizable(0, 0)
        #Vytvoření rámu nového okna
        render_mode_frame = Frame(render_mode_window, bg=mode_window_background_color)
        render_mode_frame.grid_columnconfigure(0, weight=1)
        render_mode_frame.grid_rowconfigure(0, weight=0)
        #Titulek v okně
        render_dl_mode_title = Label(render_mode_frame, text=locale['DL_MC_title'], bg=mode_window_background_color, fg=main_text_color, padx=30, pady=3, font="bold", relief='raised')
        render_dl_mode_title.grid(row=0, column=0, sticky="WE", columnspan=2)
        #Vytvoření promněnné pro více požností
        mode_value = IntVar()
        #Vytvoření možností
        render_dark_mode_toggle = Radiobutton(render_mode_frame, text=locale["dark_mode"], bg=mode_window_background_color, fg=main_text_color, padx=30, pady=5, relief='flat', activebackground=mode_window_background_color, activeforeground=main_text_color, selectcolor=mode_window_background_color, variable=mode_value, value=1, state='normal', command=lambda: self.func_appear_change(mode_value.get()), cursor='hand2')
        render_light_mode_toggle = Radiobutton(render_mode_frame, text=locale["light_mode"], bg=mode_window_background_color, fg=main_text_color, padx=30, pady=5, relief='flat', activebackground=mode_window_background_color, activeforeground=main_text_color, selectcolor=mode_window_background_color, variable=mode_value, value=0, state='normal', command=lambda: self.func_appear_change(mode_value.get()), cursor='hand2')
        render_light_mode_custom = Radiobutton(render_mode_frame, text=locale["custom"], bg=mode_window_background_color, fg=main_text_color, padx=30, pady=5, relief='flat', activebackground=mode_window_background_color, activeforeground=main_text_color, selectcolor=mode_window_background_color, state='disabled')
        render_dark_mode_toggle.grid(row=1, column=0, sticky="W", columnspan=2)
        render_light_mode_toggle.grid(row=2, column=0, sticky="W", columnspan=2)
        render_light_mode_custom.grid(row=3, column=0, columnspan=2, sticky="W")
        #Tlačítka
        render_mode_accept = Button(render_mode_frame, text=locale["DL_MAC_button"], padx=30, command=lambda: self.func_mode_reload(render_mode_window, mode_value.get()), bg=upper_bar_frame_submenu_color, fg=main_text_color, activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color, cursor='hand2')
        render_mode_cancel = Button(render_mode_frame, text=locale["DL_MCA_button"], padx=30, command=lambda: self.func_quit(render_mode_window), bg=upper_bar_frame_submenu_color, fg=main_text_color, activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color, cursor='hand2')
        render_mode_accept.grid(row=4, column=0, sticky="WS", padx=10, pady=2)
        render_mode_cancel.grid(row=4, column=1, sticky="WS", padx=10, pady=2)
        #Vykreslení rámu nového okna
        render_mode_frame.pack(fill='both', expand="True")
        
    #Funkce na vytvoření nového okna pro zěmu jazyka
    def render_locale_type_window(self):
        #Vytvoření nového okna
        render_locale_window = Toplevel()
        render_locale_window.title(locale['LT_title'])
        render_locale_window.geometry(str(data['locale_type_resolution']))
        render_locale_window.resizable(0, 0)
        #Vytvoření rámu nového okna
        render_locale_frame = Frame(render_locale_window, bg=mode_window_background_color)
        render_locale_frame.grid_columnconfigure(0, weight=1)
        render_locale_frame.grid_rowconfigure(0, weight=0)
        #Titulek v okně
        render_locale_title = Label(render_locale_frame, text=locale['L_title'], bg=mode_window_background_color, fg=main_text_color, padx=30, pady=3, font='bold', relief="raised")
        render_locale_title.grid(column=0, row=0, columnspan=2, sticky="WE")
        #Vytvoření menu možností
        ddm_var = StringVar()
        ddm_var.set(data['locale_list'][locale_default])
        render_locale_ddm = OptionMenu(render_locale_frame, ddm_var, *data['locale_list'])
        render_locale_ddm.config(bg=upper_bar_frame_submenu_color, borderwidth=0, relief='flat', fg=main_text_color, activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color, padx=50)
        render_locale_ddm.grid(row=1, column=0, pady=8, sticky="W", columnspan=2, padx=50)
        #Tlačítka
        render_mode_accept = Button(render_locale_frame, text=locale["DL_MAC_button"], padx=30, command=lambda: self.func_laguage_change(render_locale_window ,ddm_var.get()) , bg=upper_bar_frame_submenu_color, fg=main_text_color, activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color)
        render_mode_cancel = Button(render_locale_frame, text=locale["DL_MCA_button"], padx=30, command=lambda: self.func_quit(render_locale_window), bg=upper_bar_frame_submenu_color, fg=main_text_color, activebackground=upper_bar_frame_submenu_color_hover, activeforeground=main_text_color)
        render_mode_accept.grid(row=4, column=0, sticky="WS", padx=10, pady=37)
        render_mode_cancel.grid(row=4, column=1, sticky="WS", padx=10, pady=37)
        #Vykreslení rámu nového okna
        render_locale_frame.pack(fill='both', expand='true')

class Main(Render, OpenFile):
    def main(self):
        main_connected()
        global main_root
        #Hlavní vytvoření GUI
        self.main_root = Tk()
        self.main_root.title("Vojtěchovitch")
        self.main_root.geometry(str(data['main_root_resolution']))
        #Render prvků
        mode = data['dark_light_mode']
        self.render_main(mode)
        #Cyklus aplikace
        self.main_root.mainloop()

if __name__ == "__main__":
    myapp = Main()
    myapp.main()