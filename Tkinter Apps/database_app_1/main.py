#Hlavní a spuštěcí soubor aplikace Databáze
#Vkládání modulů
import tkinter
from tkinter import font
from typing import Collection #Vložení modulu "tkinter"
from tkinter import *  #Vložení všeho
from tkinter import messagebox #Vložení "messagebox"
from tkinter import filedialog #Vložení "filedialog"
from tkinter import ttk
import PIL #Vložení modulu "pillow"
from PIL import Image, ImageTk #Vložení "Image", "ImageTk"
import json

DatabaseFrameRowCons = 7
DatabaseFrameColumnCons = 7
DF_row = 1
Base_Entry = ['name', 'surname', 'bdate', 'sex', 'bunm', 'ID']

with open("./cookies.json", "r") as g:
    database_list = json.load(g)
    g.close()

def open_file():
    global file
    global database_data
    file = filedialog.askopenfilename(initialdir="/database_app_1/data", title="Vyber soubor databáze", filetypes=(("json files", "*.json"),("all files", "*.*")))
    
    #Label(Upper_line_frame, text=file).grid(row=UL_row, column=2)
    with open (file, "r") as f:
        database_data = json.load(f)
        f.close()
        reloaddatabase(True)
        
def reloaddatabase(var):
    if var == True:
        for entry in database_data:
            DatabaseButtons.grid_forget()
            DatabaseFrameBase.grid_forget()
            DatabaseFrameSystem(entry)
            DatabaseDownButtons('normal')
    else:
        DatabaseButtons.grid_forget()
        DatabaseFrameBase.grid_forget()
        DatabaseFrameSystem(Base_Entry)
        DatabaseDownButtons('disabled')
    DatabaseLabels(var)
    DatabaseCanvas.update_idletasks()
    DatabaseCanvas.yview_moveto('0.0')

def Upper_line():
    global UL_row
    global Upper_line_frame
    UL_row = 0
    Upper_line_frame = LabelFrame(root, borderwidth=1, relief=RAISED, bg="#c1c1c1")
    Upper_line_frame.grid(row=0, column=0, columnspan=16, sticky=W+E)
    open_button = Button(Upper_line_frame, text="Otevřít soubor", bg="#c1c1c1", command=open_file).grid(row=UL_row, column=0)
    motive_button = Button(Upper_line_frame, text="Upravit motiv", bg="#c1c1c1").grid(row=UL_row, column=1)
    AppendLabel = Label(Upper_line_frame, text="", bg="#c1c1c1", padx=1000).grid(row=0, column=16)
   
def DatabaseFrameSystem(entry):
    global DatabaseCanvas
    global DatabaseFrameBase
    global DatabaseFrame
    DatabaseFrameBase = LabelFrame(root, borderwidth=5, relief=SUNKEN, padx=1, pady=1)
    DatabaseFrameBase.grid(row=DF_row, column=0, pady=35) 
    
    DatabaseCanvas = Canvas(DatabaseFrameBase, width=832, height=206)
    DatabaseCanvas.grid(column=0, row=0, sticky=W)
    
    Database_yscrollbar = ttk.Scrollbar(DatabaseFrameBase, orient="vertical", command=DatabaseCanvas.yview)
    Database_yscrollbar.grid(column=9, row=0, sticky=N+S)
    
    Database_xscrollbar = ttk.Scrollbar(DatabaseFrameBase, orient=HORIZONTAL, command=DatabaseCanvas.xview)
    Database_xscrollbar.grid(column=0, row=8, sticky=W+E)
    
    DatabaseCanvas.configure(yscrollcommand=Database_yscrollbar.set, xscrollcommand=Database_xscrollbar.set)
    DatabaseCanvas.bind('<Configure>', lambda e: DatabaseCanvas.configure(scrollregion = DatabaseCanvas.bbox('all')))
    
    DatabaseFrame = Frame(DatabaseCanvas)
    DatabaseCanvas.create_window((0, 0), window=DatabaseFrame, anchor=W)
        
    corner = Label(DatabaseFrame, text=" ", font='bold', bg="black", borderwidth=2, width=15, relief='solid').grid(row=DF_row, column=0, sticky=W+E)
    
    entry_cons = 0
    DFS_row = DF_row
    DFS_column = 1+entry_cons
    while entry_cons <= len(entry)-1:
        if entry_cons == 0:
            width_set = 5
        elif entry_cons > 0 and entry_cons < 4:
            width_set = 15
        elif entry_cons > 3 and entry_cons < 6:
            width_set = 0
        else:
            width_set = 15
        headline_label = Label(DatabaseFrame, text=database_list[0][entry_cons], width=width_set, anchor=W, font='bold', bg='#9E9E9E', borderwidth=2, padx=5, relief='solid').grid(row=DFS_row, column=DFS_column+entry_cons, sticky=W+E)
        entry_cons += 1
    
    DatabaseFrameColumnCons = len(entry)
    DF_cons_y = 1
    DF_cons_x = 1
    while DF_cons_y <= DatabaseFrameRowCons:
        DF_side_label = Label(DatabaseFrame, anchor=W, text="", bg='#9E9E9E', font='bold', width=15, padx=5, pady=2, borderwidth=2, relief='solid').grid(row=DF_row+DF_cons_y, column=0)
        while DF_cons_x <= DatabaseFrameColumnCons:
            DF_mid_label = Label(DatabaseFrame, text=f"", anchor=W, borderwidth=1, padx=5, pady=3, font='bold', relief='solid').grid(row=DF_row+DF_cons_y, column=DF_cons_x, sticky=W+E)
            DF_cons_x += 1
        DF_cons_x = 1
        DF_cons_y += 1
    
def DatabaseLabels(var):
    if var == True:
        for entry in database_data:
            entry_cons = 0
            DL_row = DF_row+entry['ID']
            DL_column = 1+entry_cons
                
            User = Label(DatabaseFrame, anchor=W, text=str(entry[database_list[1][entry_cons]])+". Uživatel", bg='#9E9E9E', font='bold', width=15, padx=5, pady=2, borderwidth=2, relief='solid').grid(row=DL_row, column=0)
            ident_label = Label(DatabaseFrame, anchor=W, text="00"+str(entry[database_list[1][entry_cons]]), font='bold', padx=5, pady=3, relief='solid', borderwidth=1).grid(row=DL_row, column=DL_column, sticky=W+E)
            while entry_cons <= len(entry)-2:
                inside_label = Label(DatabaseFrame, anchor=W, text=entry[database_list[1][entry_cons+1]], font='bold', padx=5, pady=3, relief='solid', borderwidth=1).grid(row=DL_row, column=DL_column+entry_cons+1, sticky=W+E)
                entry_cons += 1
    else:
        return
                        
def DatabaseDownButtons(entry):
    global DatabaseButtons
    DBDB_row = DatabaseFrameRowCons+2
    
    DatabaseButtons = LabelFrame(DatabaseFrameBase, relief=FLAT)
    DatabaseButtons.grid(row=DBDB_row, column=0, columnspan=9, sticky=W)
    
    new_user_btn = Button(DatabaseButtons, text="Nový uživatel", anchor=W, relief=RAISED, bg="#c1c1c1", borderwidth=3, command=new_user_window, state=entry).grid(row=DBDB_row, column=1, padx=5)
    edit_user_btn = Button(DatabaseButtons, text="Upravit uživatele", anchor=W, relief=RAISED, bg="#c1c1c1", borderwidth=3, state=entry).grid(row=DBDB_row, column=2, padx=5)
    open_user_btn = Button(DatabaseButtons, text="Otevřít užvatele", anchor=W, relief=RAISED, bg="#c1c1c1", borderwidth=3, state=entry).grid(row=DBDB_row, column=3, padx=5)
    delete_user_bnt = Button(DatabaseButtons, text="Smazat uživatele", anchor=W, relief=RAISED, bg="#c1c1c1", borderwidth=3, state=entry).grid(row=DBDB_row, column=4, padx=5)

def new_user_window():
    NewUserWindow = Toplevel()
    NewUserWindow.title("Nový uživatel")
    NewUserWindow.tk.call('wm', 'iconphoto', NewUserWindow._w, tkinter.PhotoImage(file='app.png'))
    NewUserWindow.geometry("858x480")
    NewUserWindow.resizable(0,0)
    
    NewUserFrameBase = LabelFrame(NewUserWindow, borderwidth=5, relief=SUNKEN, padx=1, pady=1)
    NewUserFrameBase.grid(row=0, column=0, pady=35, padx=35) 
    
    NewUserCanvas = Canvas(NewUserFrameBase, width=480, height=132)
    NewUserCanvas.grid(column=0, row=0, sticky=W)
    NewUser_yscrollbar = ttk.Scrollbar(NewUserFrameBase, orient="vertical", command=NewUserCanvas.yview)
    NewUser_yscrollbar.grid(column=3, row=0, sticky=N+S)
    NewUserCanvas.configure(yscrollcommand=NewUser_yscrollbar.set)
    NewUserCanvas.bind('<Configure>', lambda e: NewUserCanvas.configure(scrollregion = NewUserCanvas.bbox('all')))
    
    NewUserFrame = Frame(NewUserCanvas)
    NewUserCanvas.create_window((0, 0), window=NewUserFrame, anchor=W)
    
    NewUserEntry = []
    data = {}
    entry_cons = 0
    for entry in database_data:
        while entry_cons < len(entry):
            if database_list[1][entry_cons] in entry:
                if database_list[1][entry_cons] == "ID":
                    entry_cons += 1
                    pass
                else:
                    lbl = Label(NewUserFrame, text=database_list[0][entry_cons], borderwidth=1, relief=SOLID, font='bold', width=20)
                    lbl.grid(column=0, row=entry_cons, sticky=W+E)
                    entr = Entry(NewUserFrame, font='bold', relief=SOLID)
                    entr.grid(column=1, row=entry_cons, sticky=E+W)
                    NewUserEntry.append(entr)
                    entry_cons += 1
            else:
                entry_cons += 1
    
    def NewUserAdd():
        for entry in database_data:
            add_cons = 0
            while add_cons < len(entry):
                if database_list[1][add_cons] in entry:
                    if database_list[1][add_cons] == "ID":
                        ident_cons = 1
                        while True:
                            if ident_cons <= entry["ID"]:
                                ident_cons += 1
                                continue
                            else:
                                break
                        data["ID"] = ident_cons
                        add_cons += 1
                        pass
                    else:
                        add_cons = 1
                        for entries in NewUserEntry:
                            data[database_list[1][add_cons]] = str(entries.get())
                            add_cons += 1
                else:
                    add_cons += 1
            database_data.append(data)
            with open (file, "w") as f:
                json.dump(database_data, f, indent=8)
                f.close()
            break
    
    NewUserButton = Button(NewUserWindow, text="Přidat uživatele", command=NewUserAdd)
    NewUserButton.grid(row=entry_cons, column=0)
    CancelButton = []

def main():
    global root
    root = Tk()
    root.title("database")
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='app.png'))
    root.geometry("1700x900")
    root.resizable(0, 0)
    
    DatabaseFrameSystem(Base_Entry)
    DatabaseDownButtons('disabled')
    Upper_line()
    
    root.mainloop()
    
main()