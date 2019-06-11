import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter
from tkinter import filedialog


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
    return obraz

def opcje_skalowanie2():
    global obraz
    obraz=obraz.resize((150,212))
    plotno.obrazek=ImageTk.PhotoImage(obraz)
    plotno.itemconfig(moj_obrazek, image=plotno.obrazek)
    return obraz

def opcje_skalowanie3():
    global obraz
    obraz=obraz.resize((214,232))
    plotno.obrazek=ImageTk.PhotoImage(obraz)
    plotno.itemconfig(moj_obrazek, image=plotno.obrazek)
    return obraz

#funkcje-filtry 
def czarno_bialy():
    global obraz
    obraz=obraz.convert("L")
    plotno.obrazek=ImageTk.PhotoImage(obraz)
    plotno.itemconfig(moj_obrazek, image=plotno.obrazek)

def rozmycie():
    global obraz
    obraz=obraz.filter(ImageFilter.BLUR)
    plotno.obrazek=ImageTk.PhotoImage(obraz)
    plotno.itemconfig(moj_obrazek, image=plotno.obrazek)

def emboss():
    global obraz
    obraz=obraz.filter(ImageFilter.EMBOSS)
    plotno.obrazek=ImageTk.PhotoImage(obraz)
    plotno.itemconfig(moj_obrazek, image=plotno.obrazek)

#Funkcja pozwala na wczytanie dowolnego pliku, domyślnie o formacie .jpg z komputera użytkownika 
def wczytaj_plik():
    global obraz
    global moj_obrazek
    glowneOkno.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files",".jpg"),("all files",".*")))
    obraz = Image.open(glowneOkno.filename)
    obrazTk = ImageTk.PhotoImage(obraz)
    plotno.obrazek=obrazTk
    moj_obrazek=plotno.create_image(200 ,200 ,image=obrazTk)

#Funkcja zapisuje plik w formacie .jpg, pod nazwą podaną przez użytkownika
def zapisz_plik():
    global obraz
    save_path = filedialog.asksaveasfilename(initialdir = "/", title = "Select file", filetypes = (("JPG",".jpg"),("Wszystkie pliki",".*")))
    save_path+=".jpg"
    obraz.save(save_path)

#funkcja zamykająca
def zamknij():
    global glowneOkno
    glowneOkno.destroy()
    
    
glowneOkno = Tk()
pasekMenu = Menu(glowneOkno) 

plotno=Canvas(glowneOkno, width=1000 ,height=750)
plotno.pack()

plikMenu = Menu(pasekMenu, tearoff = 0) #przycisk plik na pasku menu
pasekMenu.add_cascade(label="Plik" , menu = plikMenu) #umożliwia się rozwinięcie przyciskowi plik

plikMenu.add_command(label = "Wczytaj plik", command=wczytaj_plik) #przycisk umożliwiający wczytanie obrazu
plikMenu.add_command(label = "Zapisz plik" , command=zapisz_plik) #przycisk umożliwiający zapisanie nowego obrazu
plikMenu.add_command(label = "Zamknij program" , command=zamknij) #przycisk zamykający program


opcjeMenu = Menu(pasekMenu, tearoff = 0) #tworzy przycisk opcje w pasku menu
obrotObrazu = Menu(opcjeMenu, tearoff = 0) 
skalujObraz = Menu(opcjeMenu, tearoff = 0)
filtryMenu=Menu(opcjeMenu, tearoff = 0)

pasekMenu.add_cascade(label="Opcje" , menu = opcjeMenu) #umożliwia rozwinięcie się przyciskowi opcje
opcjeMenu.add_cascade(label="Obrót obrazu" , menu = obrotObrazu) #Wumożliwia rozwinięcie się przyciskowi obrót obrazu
obrotObrazu.add_command(label = "Obrót 90" , command=obrot_90) #przycisk wywołujący obrót obrazu o 90 stopni
obrotObrazu.add_command(label = "Obrót 180" , command=obrot_180) #przycisk wywołujący obrót obrazu o 180 stopni
obrotObrazu.add_command(label = "Obrót 270" , command=obrot_270) #przycisk wywołujący obrót obrazu o 270 stopni

opcjeMenu.add_cascade(label = "Skaluj" , menu = skalujObraz) #umożliwia rozwinięcie się przyciskowi skaluj
skalujObraz.add_command(label="101x150", command=opcje_skalowanie1) #przycisk wywołujący skalowanie obrazu na wymiary 101x150 pikseli
skalujObraz.add_command(label="150x212", command=opcje_skalowanie2) #przycisk wywołujący skalowanie obrazu na wymiary 150x212 pikseli
skalujObraz.add_command(label="214x232", command=opcje_skalowanie3) #przycisk wywołujący skalowanie obrazu na wymiary 214x232 pikseli

opcjeMenu.add_cascade(label="Filtry", menu=filtryMenu) #umożliwia rozwinięcie się przyciskowi filtry
filtryMenu.add_command(label="Czarno-biały", command=czarno_bialy) #przycisk wywołujący nałożenie filtra: czarno-biały
filtryMenu.add_command(label="Rozmycie", command=rozmycie) #przycisk wywołujący nałożenie filtra: rozmycie
filtryMenu.add_command(label="Negatyw", command=emboss) #przycisk wywołujący nałożenie filtra: negatyw

glowneOkno.config(menu=pasekMenu)
glowneOkno.mainloop()

