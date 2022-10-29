# coding: utf-8

import tkinter as tk
import numpy as np

from tkinter import *
from tkinter import messagebox

from time import strftime

# Classe du projet
class Graphes (tk.Tk):

    # Déclaration et initialisation de la fenêtre
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("MBD - Métro, boulot, dodo")  # Titre
        self.iconphoto(False, tk.PhotoImage(file='../venv/Images/icon.ico')) #Icon
        self.config(bg='#49A')  # Couleur d'arrière plan
        self.parametre_fenetre()    # Dimensionnement de la fenêtre
        self.fenetre_principale()   # Appel de la fenêtre principale

    # Dimensionnement de la fenêtre
    def parametre_fenetre(self):

        # Récupération de la taille de l'écran
        taille_ecran = self.winfo_screenheight()
        largeur_ecran = self.winfo_screenwidth()

        # Dimensionnement de la fenêtre
        self.taille_fenetre = 916
        self.largeur_fenetre = 1114

        x = int((largeur_ecran / 2) - (self.largeur_fenetre / 2))
        y = int((taille_ecran / 2) - (self.taille_fenetre / 2))

        self.geometry("{}x{}+{}+{}".format(self.largeur_fenetre, self.taille_fenetre, x, y))

    # Fenêtre principale
    def fenetre_principale(self):

        # Canevas principal du dessus
        self.canevas_principal_1 = tk.Canvas(self, bg='#49A')   # Déclaration et initialisation
        self.canevas_principal_1.config(highlightthickness=0)   # Bordures enlevées
        self.canevas_principal_1.pack(ipadx=50, ipady=50, fill=tk.X, expand=True)   # Affichage du canevas

        # Sous-canevas gauche pour le logo
        self.canevas_principal_1_logo = tk.Canvas(self.canevas_principal_1, bg="white", height=10, width=10)
        self.canevas_principal_1_logo.config(highlightthickness=0)
        self.canevas_principal_1_logo.pack(ipadx=10, ipady=1., expand=True, fill=tk.BOTH, side=tk.LEFT)

        # Affichage du logo dans le sous-canevas gauche
        terre = PhotoImage(file='../venv/Images/icon.ico')   # Récupération de l'image
        self.canevas_principal_1_logo.create_image(1, 1, image=terre)   # Création de l'image
        self.canevas_principal_1_logo.pack(expand=True) # Affichage de l'image

        # Sous-canevas à droite pour les boutons
        self.canevas_principal_1_boutons = tk.Canvas(self.canevas_principal_1, bg='white', height=10, width=10)
        self.canevas_principal_1_boutons.config(highlightthickness=0)
        self.canevas_principal_1_boutons.pack(ipadx=50, ipady=100, expand=True, fill=tk.BOTH, side=tk.LEFT)

        # Affichage des boutons dans le sous-canevas droit
        self.bouton_trajet = Button(self.canevas_principal_1_boutons, text="Trajet", command=self.fenetre_pcc)
        self.bouton_trajet.pack(ipadx=20, ipady=5, expand=True)

        self.bouton_arbre = Button(self.canevas_principal_1_boutons, text="Arbre couvrant", command=self.fenetre_acpm)
        self.bouton_arbre.pack(ipadx=20, ipady=10, expand=True)

        # Canevas principal du dessous pour l'affichage de l'heure
        self.canevas_principal_2 = tk.Canvas(self, bg='#49A')
        self.canevas_principal_2.config(highlightthickness=0)
        self.canevas_principal_2.pack(ipadx=20, ipady=170, fill=tk.X, expand=True)

        # Affichage de l'heure
        self.lbl = Label(self.canevas_principal_2, font=('calibri', 80, 'bold'), fg='white', bg='#49A')
        self.lbl.pack(ipadx=50,ipady=50,expand=True)
        self.time()

        # Mise à jour de la fenêtre
        self.mainloop()

    # Fonction pour récupérer l'heure
    def time(self):
        string = strftime('%H:%M:%S')   # Convertit un tuple temporel en chaîne selon une spécification de format.
        self.lbl.config(text=string)    # Configuration du format
        self.lbl.after(1000, self.time) # Permet de faire avancer le temps

    # Fenêtre du plus court chemin
    def fenetre_pcc(self):

        # Variable globale pour compter le nombre de clics pour le choix des stations
        global compteur
        compteur = 0

        # Libération des composants de l'ancienne fenêtre
        self.canevas_principal_1.pack_forget()
        self.canevas_principal_1_logo.pack_forget()
        self.canevas_principal_1_boutons.pack_forget()
        self.canevas_principal_2.pack_forget()
        self.bouton_trajet.pack_forget()
        self.bouton_arbre.pack_forget()

        self.title("MBD - Plus court chemin entre deux stations")  # Titre

        # Canevas gauche
        self.canv = tk.Canvas(self, bg='#49A', height=self.taille_fenetre)
        self.canv.config(highlightthickness=0)
        self.canv.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=False, side=tk.LEFT)

        point = self.bind('<Button-1>', self.activation)    # Création d'un point si un clique intervient
        # Suivant le fichier texte exploité, les données pourront être en lien avec les cliques

        # Création du bouton recommencer qui permet d'effacer les stations sélectionnées
        self.bouton_recommencer = tk.Button(self.canv, text="Recommencer", command=self.recommencer_pcc())
        self.bouton_recommencer.pack(side=tk.TOP, pady=15)
        self.bouton_retour = tk.Button(self.canv, text="Retour", command=self.retour)
        self.bouton_retour.pack(side=tk.BOTTOM, pady=15)

        # Carte du métro
        metro = PhotoImage(file='../venv/Images/metro.png')
        self.canevas = Canvas(self, width=self.largeur_fenetre, height=self.taille_fenetre)
        self.canevas.create_image(1, 1, anchor=NW, image=metro)
        self.canevas.config(highlightthickness=0)
        self.canevas.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True)

        self.mainloop()

    # Fonction qui permet de sélectionner une station
    def activation(self, event):

        # Variable globale pour compter le nombre de clics pour le choix des stations
        global compteur
        NomStation = ["",""]
        ID_Gare = [0,0]

        # Récupération des coordonnées du clique
        x = event.x - 5
        y = event.y - 5 + 40

        # Définition du diamètre du nouveau point (station)
        diametre = 12

        # Si moins de deux stations sont sélectionnées, création d'un point, sinon message d'erreur
        if compteur < 2:

            dicoCoordonnees = {}
            fichier = open(
                "C:\\Users\\lucqu\\OneDrive\\Documents\\efrei\\L3\\graphe\\Graphes\\venv\\Data\\pospoints.txt", "r",
                encoding="utf-8")
            gare_data = fichier.readlines()
            characters = "\n"

            for i in range(482):
                coordonnees_x = gare_data[i].split(";")[0]
                coordonnees_y = gare_data[i].split(";")[1]
                nom_gare = gare_data[i].split(";")[2]
                nom_gare = nom_gare.replace(characters[0], "")
                nom_gare = nom_gare.split("@")
                temp = ""
                for i in range(len(nom_gare)):
                    temp = temp+nom_gare[i]
                nom_gare = temp
                dicoCoordonnees[str(i)] = [coordonnees_x, coordonnees_y, nom_gare]

            print(dicoCoordonnees)



            # Vérifications par des if du bon placement du clique qui doit être sur la carte
            if x > 125 :
                for i in range(482):
                    print(int(dicoCoordonnees[str(5)][0]))
                    if ((x < int(dicoCoordonnees[str(i)][0]) + 5 and x > int(dicoCoordonnees[str(i)][0]) - 5) and (
                            y < int(dicoCoordonnees[str(i)][1]) + 5 and y > int(dicoCoordonnees[str(i)][1]) - 5)):
                        point = self.canevas.create_oval(x, y - 40, diametre + x, diametre + y - 40, fill="cyan",
                                                         width=2)  # Affichage du point
                        compteur += 1
                        Nom_station[compteur-1] = dicoCoordonnees[str(i)][2]

            else :
                if y >= 35 and y <= 865:
                    messagebox.showwarning("Attention !", "Cliquer sur la carte")

        else :

            fichier = open("C:\\Users\\lucqu\\PycharmProjects\\graphe\\metro.txt", "r", encoding="utf-8")
            lignes = fichier.readlines()
            dicoGare = {}
            dicoGare_Id = []
            cpt = 0
            for x in lignes:

                if x[:1] == 'V' and x.split()[1] != "num_sommet":
                    nomStation_global = x.split(";")[0].split()
                    del nomStation_global[0]  # on supprime 'V'
                    data_gare = [nomStation_global[0], ""]

                    for i in range(1, len(nomStation_global)):
                        data_gare[1] = data_gare[1] + (nomStation_global[i])
                        if (i < len(nomStation_global) - 1):
                            data_gare[1] = data_gare[1] + ' '

                    deja_dedans = False
                    for i in range(len(dicoGare)):
                        if (data_gare[1] == dicoGare[i]):
                            deja_dedans = True
                            id_existant = i
                    if (deja_dedans != True):
                        dicoGare.update({cpt: data_gare[1]})
                        dicoGare_Id.append([cpt, int(data_gare[0])])
                        cpt += 1
                    else:
                        dicoGare_Id.append([id_existant, int(data_gare[0])])

            for i in range(len(dicoGare)):
                if(dicoGare[i][1] == Nom_Sation[0]):
                    ID_Gare[0] = i
                if (dicoGare[i][1] == Nom_Sation[1]):
                    ID_Gare[1] = i

            print(NomStation)
            print(ID_Gare)

            if x > 100:
                messagebox.showerror("Erreur !", "Deux stations déjà sélectionnées !")

    # Fonction qui permet d'effacer les stations sélectionnées pour le plus court chemin et recommencer
    def recommencer_pcc(self):
        self
        # A COMPLETER

    # Fonction qui permet d'effacer la station sélectionnée pour l'arbre couvrant de poids minimum pour recommencer
    def recommencer_acpm(self):
        self

    # Fonction permettant de revenir à la fenêtre principale
    def retour(self):
        self.destroy()
        self.__init__()

    # Fenêtre de l'arbre couvrant de poids minimum
    def fenetre_acpm(self):

        # Variable globale pour compter le nombre de clics pour le choix des stations
        global compteur
        compteur = 0

        # Libération des composants de l'ancienne fenêtre
        self.canevas_principal_1.pack_forget()
        self.canevas_principal_1_logo.pack_forget()
        self.canevas_principal_1_boutons.pack_forget()
        self.canevas_principal_2.pack_forget()
        self.bouton_trajet.pack_forget()
        self.bouton_arbre.pack_forget()
        self.title("MBD - Arbre couvrant de poids minimum")  # Titre

        self.canv = tk.Canvas(self, bg='#49A', height=self.taille_fenetre)
        self.canv.config(highlightthickness=0)
        self.canv.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=False, side=tk.LEFT)

        self.bouton_recommencer = tk.Button(self.canv, text="Recommencer", command=self.recommencer_acpm())
        self.bouton_recommencer.pack(side=tk.TOP, pady=15)
        self.bouton_retour = tk.Button(self.canv, text="Retour", command=self.retour)
        self.bouton_retour.pack(side=tk.BOTTOM, pady=15)

        # Carte du métro
        metro = PhotoImage(file='../venv/Images/metro.png')
        self.canevas = Canvas(self, width=self.largeur_fenetre, height=self.taille_fenetre)
        self.canevas.create_image(1, 1, anchor=NW, image=metro)
        self.canevas.config(highlightthickness=0)
        self.canevas.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True)

        self.bind('<Button-1>', self.activation)

        self.mainloop()