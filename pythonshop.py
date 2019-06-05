from tkinter import *
from tkinter import messagebox

glowneOkno = Tk()
pasekMenu = Menu(glowneOkno)

plikMenu = Menu(pasekMenu, tearoff = 0)
pasekMenu.add_cascade(label="Plik" , menu = plikMenu)

plikMenu.add_command(label = "Wczytaj plik" , command=wczytaj_plik)
plikMenu.add_command(label = "Zapisz plik" , command=zapisz_plik)
plikMenu.add_command(label = "Zamknij program" , command=zamknij)

opcjeMenu = Menu(pasekMenu, tearoff = 0)
pasekMenu.add_cascade(label="Opcje" , menu = opcjeMenu)

opcjeMenu.add_command(label = "Obrót 90" , command=obrot_90)
opcjeMenu.add_command(label = "Obrót 180" , command=obrot_180)
opcjeMenu.add_command(label = "Obrót 270" , command=obrot_270)
opcjeMenu.add_command(label = "Skaluj" , command=opcja_skalowanie)
opcjeMenu.add_command(label = "Czarno biały obraz" , command=czarno_bialy)

glowneOkno.config(menu=pasekMenu)
glowneOkno.mainloop()
