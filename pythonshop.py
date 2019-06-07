import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def obrot_90():
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

glowneOkno = Tk()
pasekMenu = Menu(glowneOkno)
plotno=Canvas(glowneOkno, width=400 ,height=400)
plotno.pack()
obraz=Image.open("1.jpg")
obrazTk=ImageTk.PhotoImage(obraz)
plotno.obrazek=obrazTk
moj_obrazek=plotno.create_image(200 ,200 ,image=obrazTk)

plikMenu = Menu(pasekMenu, tearoff = 0)
pasekMenu.add_cascade(label="Plik" , menu = plikMenu)

'''
plikMenu.add_command(label = "Wczytaj plik")
plikMenu.add_command(label = "Zapisz plik" , command=zapisz_plik)
plikMenu.add_command(label = "Zamknij program" , command=zamknij)
'''
opcjeMenu = Menu(pasekMenu, tearoff = 0)
pasekMenu.add_cascade(label="Opcje" , menu = opcjeMenu)

opcjeMenu.add_command(label = "Obrót 90" , command=obrot_90)
opcjeMenu.add_command(label = "Obrót 180" , command=obrot_180)
opcjeMenu.add_command(label = "Obrót 270" , command=obrot_270)
'''
opcjeMenu.add_command(label = "Skaluj" , command=opcja_skalowanie)
opcjeMenu.add_command(label = "Czarno biały obraz" , command=czarno_bialy)
'''
glowneOkno.config(menu=pasekMenu)
glowneOkno.mainloop()
