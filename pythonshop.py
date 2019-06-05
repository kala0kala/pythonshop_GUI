from tkinter import *
from tkinter import messagebox

glowneOkno = Tk()
pasekMenu = Menu(glowneOkno)
plotno=Canvas(glowneOkno, width=400 ,height=400)
plotno.pack()
obraz=Image.open("1.jpg")
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(200 ,200 ,image=obrazTk)

plikMenu = Menu(pasekMenu, tearoff = 0)
pasekMenu.add_cascade(label="Plik" , menu = plikMenu)

plikMenu = Menu(pasekMenu, tearoff = 0)
pasekMenu.add_cascade(label="Plik" , menu = plikMenu) #w menu tworzy pasek opcji o nazwie "Plik"

plikMenu.add_command(label = "Wczytaj plik" , command=wczytaj_plik) # w pasku "Plik" tworzy przycisk do wczytania pliku
plikMenu.add_command(label = "Zapisz plik" , command=zapisz_plik) # w pasku "Plik" tworzy przycisk do zapisania pliku
plikMenu.add_command(label = "Zamknij program" , command=zamknij) # w pasku "Plik" tworzy przycisk do zamknięcia programu

opcjeMenu = Menu(pasekMenu, tearoff = 0)
pasekMenu.add_cascade(label="Opcje" , menu = opcjeMenu) #w menu tworzy pasek opcji o nazwie "Opcje"

opcjeMenu.add_command(label = "Obrót 90" , command=obrot_90) # w pasku "Opcje" tworzy przycisk do obrotu obrazu o 90 stopni
opcjeMenu.add_command(label = "Obrót 180" , command=obrot_180) # w pasku "Opcje" tworzy przycisk do obrotu obrazu o 180 stopni
opcjeMenu.add_command(label = "Obrót 270" , command=obrot_270) # w pasku "Opcje" tworzy przycisk do obrotu obrazu o 270 stopni
opcjeMenu.add_command(label = "Skaluj" , command=opcja_skalowanie) # w pasku "Opcje" tworzy przycisk do skalowania obrazu
opcjeMenu.add_command(label = "Czarno biały obraz" , command=czarno_bialy) # w pasku "Opcje" tworzy przycisk do zmiany kolorów obrazu na czarno-białe

glowneOkno.config(menu=pasekMenu)
glowneOkno.mainloop()
