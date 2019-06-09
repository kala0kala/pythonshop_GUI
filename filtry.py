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
