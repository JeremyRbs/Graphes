from tkinter import *
from random import *


def pointeur(event):
    global chaine, posx, posy, CANEVAS, logo_os, compteur_point, compteur_tour, fen
    if posx <= event.x <= posx + 100 and posy <= event.y <= posy + 100:
        Label(CANEVAS, image=logo_os).place(x=posx, y=posy)
        compteur_point += 10 - compteur_tour
        compteur_tour = 10
        chaine.configure(text="\nGAGNE !!!" + "       nombre de points: " + str(compteur_point), font='Arial 14')
        CANEVAS.place(x=0, y=70)
    else:
        chaine.configure(text="PERDU          tour: " + str(compteur_tour) + "\nFLAIR:     est à " + str(
            abs(posx + 50 - event.x)) + " en largeur et à " + str(abs(posy + 50 - event.y)) + " en hauteur de l'os",
                         font='Arial 13')
        compteur_tour += 1
        if compteur_tour > 10:
            CANEVAS.place(x=0, y=70)
            fen.destroy()


def jouer():
    global chaine, posx, posy, CANEVAS, logo_os, compteur_point, compteur_tour, fen
    compteur_point = 0
    for jeu in range(0, 1000):
        fen = Tk()
        fen.geometry('580x630')
        logo_os = PhotoImage(file='C:\\Users\\Jerem\\PycharmProjects\\Graphes\\venv\\Images\\icon.ico')

        #background
        CANEVAS = Canvas(fen, width=580, height=500, bg='white')
        terre = PhotoImage(file='C:\\Users\\Jerem\\PycharmProjects\\Graphes\\venv\\Images\\metro.png')
        CANEVAS.create_image(1, 1, anchor=NW, image=terre)
        CANEVAS.place(x=0, y=70)

        #titre
        CANEVAS_HAUT = Canvas(fen, width=80, height=70)
        titre = PhotoImage(file='C:\\Users\\Jerem\\PycharmProjects\\Graphes\\venv\\Images\\icon.ico')
        CANEVAS_HAUT.create_image(1, 1, anchor=NW, image=titre)
        CANEVAS_HAUT.place(x=0, y=0)

        #bas
        CANEVAS_BAS = Canvas(fen, width=120, height=60, bg='blue')
        argent = PhotoImage(file='C:\\Users\\Jerem\\PycharmProjects\\Graphes\\venv\\Images\\icon.ico')
        CANEVAS_BAS.create_image(1, 1, anchor=NW, image=argent)
        CANEVAS_BAS.place(x=460, y=570)

        compteur_tour = 0
        posx = randint(0, 540)
        posy = randint(0, 545)
        print(posx, posy)
        chaine = Label(fen)
        chaine.place(x=0, y=570)
        CANEVAS.bind("<Button-1>", pointeur)
        CANEVAS.place(x=0, y=70)
        fen.mainloop()


jouer()