import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk



def obrot_90(): #funkcja obracająca obraz o 90 stopni
    global obraz
    obraz = obraz.rotate(90)
    plotno.obrazek=ImageTk.PhotoImage(obraz)
    plotno.itemconfig(moj_obrazek, image=plotno.obrazek)

def obrot_180(): #funkcja obracająca obraz o 180 stopni
    global obraz
    obraz = obraz.rotate(180)
    plotno.obrazek=ImageTk.PhotoImage(obraz)
    plotno.itemconfig(moj_obrazek, image=plotno.obrazek)

def obrot_270(): #fynkcja obracająca obraz o 270 stopni
    global obraz
    obraz = obraz.rotate(270)
    plotno.obrazek=ImageTk.PhotoImage(obraz)
    plotno.itemconfig(moj_obrazek, image=plotno.obrazek)
 
#Trzy różne skalowania w trzech różnych funkcjach
def opcje_skalowanie1():
    global obraz
    obraz=obraz.resize((101,150))
    plotno.obrazek=ImageTk.PhotoImage(obraz)
    plotno.itemconfig(moj_obrazek, image=plotno.obrazek)
    print("Przeskalowano!")
    return obraz

def opcje_skalowanie2():
    global obraz
    obraz=obraz.resize((150,212))
    plotno.obrazek=ImageTk.PhotoImage(obraz)
    plotno.itemconfig(moj_obrazek, image=plotno.obrazek)
    print("Przeskalowano!")
    return obraz

def opcje_skalowanie3():
    global obraz
    obraz=obraz.resize((214,232))
    plotno.obrazek=ImageTk.PhotoImage(obraz)
    plotno.itemconfig(moj_obrazek, image=plotno.obrazek)
    print("Przeskalowano!")
    return obraz

glowneOkno = Tk()
pasekMenu = Menu(glowneOkno)
obrotObrazu = Menu(pasekMenu)
skalujObraz = Menu(pasekMenu)
plotno=Canvas(glowneOkno, width=1000 ,height=750)
plotno.pack()
obraz=Image.open("1.jpg")
obrazTk=ImageTk.PhotoImage(obraz)
plotno.obrazek=obrazTk
moj_obrazek=plotno.create_image(200 ,200 ,image=obrazTk)

plikMenu = Menu(pasekMenu, tearoff = 0) #paek menu
pasekMenu.add_cascade(label="Plik" , menu = plikMenu)

'''
plikMenu.add_command(label = "Wczytaj plik")
plikMenu.add_command(label = "Zapisz plik" , command=zapisz_plik)

plikMenu.add_command(label = "Zamknij program" , command=zamknij)
''' 

opcjeMenu = Menu(pasekMenu, tearoff = 0)
obrotObrazu = Menu(opcjeMenu, tearoff = 0)
skalujObraz = Menu(opcjeMenu, tearoff = 0)
pasekMenu.add_cascade(label="Opcje" , menu = opcjeMenu)
opcjeMenu.add_cascade(label="Obrót obrazu" , menu = obrotObrazu)
obrotObrazu.add_command(label = "Obrót 90" , command=obrot_90)
obrotObrazu.add_command(label = "Obrót 180" , command=obrot_180)
obrotObrazu.add_command(label = "Obrót 270" , command=obrot_270)

opcjeMenu.add_cascade(label = "Skaluj" , menu = skalujObraz)
skalujObraz.add_command(label="101x150", command=opcje_skalowanie1)
skalujObraz.add_command(label="150x212", command=opcje_skalowanie2)
skalujObraz.add_command(label="214x232", command=opcje_skalowanie3)

'''
opcjeMenu.add_command(label = "Czarno biały obraz" , command=czarno_bialy)
'''
glowneOkno.config(menu=pasekMenu)
glowneOkno.mainloop()

