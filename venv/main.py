# coding: utf-8

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np

from time import strftime
from Windows.home import Graphes
#from Algorithms.pcc import *
#from Algorithms.acpm import *

def ExistChemin(matriceAdj, u, v):
    n = len(matriceAdj)  # nombre de sommets
    file = []
    visites = [False] * n
    file.append(u)
    while file:
        courant = file.pop(0)
        visites[courant] = True
        for i in range(n):
            if matriceAdj[courant][i] > 0 and visites[i] == False:
                file.append(i)
                visites[i] = True

            # Si i est un noeud adjacent et égal à v (destination)
            # donc il existe un chemin de u à i
            elif matriceAdj[courant][i] > 0 and i == v:
                return True
    # pas de chemin entre u et v
    return False


def estCycle(matriceAdj, u):
    n = len(matriceAdj)
    file = []
    visites = [False] * n
    visites[u] = True

    # Pour mémoriser à partir de quel sommet nous avons découvert chaque sommet du graphe
    parent = [-1] * n

    # Au départ le parent de u est u lui même
    parent[u] = u

    file.append(u)
    while file:
        courant = file.pop(0)
        visites[courant] = True
        for i in range(n):
            if matriceAdj[courant][i] > 0 and visites[i] == False:
                file.append(i)
                visites[i] = True

                # Parent de i et le noeud courant
                parent[i] = courant

            # Si "i" est un noeud adjacent, déjà visité et "i" n'est pas le parent de courant
            # Donc il y'a un cycle, retourner True
            elif matriceAdj[courant][i] > 0 and visites[i] == True and parent[courant] != i:
                return True

    return False


def nappartient_pas_a_T(j, T):
    for i in range(len(T)):
        if (j == T[i]["sommet_darrive"]):
            return False
    return True

def nappartient_pas_a_V(j, V):
    for i in range(len(V)):
        if(j == V[i]["sommet_darrive"]):
            return False
    return True

def afficher_list(list):
    for i in range(len(list)):
        print("list[",i,"] = ", list[i])


def Kruskal(Matrice):
    copie_matrice = Matrice
    matrice_obtenu = np.zeros((376, 376))
    min = {"poids": 1000, "sommet_dorigine": 0, "sommet_darrive": 0};
    T = list()
    V = list()

    for k in range(0,376):
        for i in range(0, 376):
            for j in range(0, 376):
                if (copie_matrice[i][j] != 0):
                    if (copie_matrice[i][j] < min["poids"] and nappartient_pas_a_V(j, V)):

                        min["poids"] = copie_matrice[i][j]
                        min["sommet_dorigine"] = i
                        min["sommet_darrive"] = j

        V.append({"poids":min["poids"], "sommet_dorigine":min["sommet_dorigine"], "sommet_darrive":min["sommet_darrive"]})
        min["poids"] = 1000


    for i in range(0,len(V)-1):
        matrice_obtenu[V[i]["sommet_dorigine"]][V[i]["sommet_darrive"]] = V[i]["poids"]
        if(nappartient_pas_a_T(V[i]["sommet_darrive"], T) and not estCycle(matrice_obtenu, V[i]["sommet_darrive"])):
            T.append(V[i])
        elif(estCycle(matrice_obtenu, V[i]["sommet_darrive"])):
            matrice_obtenu[V[i]["sommet_dorigine"]][V[i]["sommet_darrive"]] = 0
    return T

def somme(tab):
    somme = 0
    for i in range(0,len(tab)):
        somme += tab[i]["poids"]
    return somme



def estConnexe(matrice, pointDep):
    n = len(matrice)  # nombre de sommets dans le graphe
    tabVisite = [];
    file = [pointDep];
    while file:
        current = file.pop(0)
        tabVisite.append(current);
        for i in range(n):
            if i != current and (matrice[current][i] > 0 or matrice[i][current] > 0) and i not in tabVisite:
                file.append(i);
        if len(tabVisite) == n:
            return True
    return False





def afficheTrajet(predecesseurs, depart, fin, trajet):
    if fin == depart:
        print("Vous partez de " + nomSommet[int(depart)])
        for station in trajet:
            print("puis allez à " + nomSommet[int(station)])
    else:
        (afficheTrajet(predecesseurs, depart, predecesseurs[fin], [fin] + trajet))

def plusCourt(graphe, stationDep, stationEnCours, stationArr, visites, distances, predecesseurs):
    if stationEnCours == stationArr: #Nous sommes arrivés
        afficheTrajet(predecesseurs, stationDep, stationArr, [])
        return distances[stationEnCours]
    if  len(visites) == 0 :
        distances[stationEnCours] = 0
    for voisin in graphe[stationEnCours]:
        if voisin not in visites:
            # la distance est soit la distance calculée précédemment soit l'infini
            dist_voisin = distances.get(voisin, float('inf'))
            # on calcule la nouvelle distance calculée en passant par l'étape
            new_dist = distances[stationEnCours] + graphe[stationEnCours][voisin]
            if new_dist < dist_voisin:
                distances[voisin] = new_dist
                predecesseurs[voisin] = stationEnCours
    visites.append(stationEnCours)

    non_visites = dict((s, distances.get(s, float('inf'))) for s in graphe if s not in visites)
    prochaineStation = min(non_visites, key=non_visites.get)
    return plusCourt(graphe, stationDep,  prochaineStation, stationArr, visites, distances, predecesseurs)

def dijkstra(graphe,stationDep, stationArr):
   return plusCourt(graphe, stationDep, stationDep, stationArr, [], {}, {})

# Main permettant de lancer le programme
if __name__ == "__main__":

    fichier = open("C:\\Users\\lucqu\\PycharmProjects\\graphe\\metro.txt", "r", encoding="utf-8")
    lignes = fichier.readlines()
    dicoGraphe = {}
    nomSommet = {}
    for i in range(376):
        dicoGraphe[str(i)] = {}

    for x in lignes:
        if x[:1] == 'E' and x.split()[1] != "num_sommet1":
            dicoGraphe[str(x.split()[1])][str(x.split()[2])] = int(x.split()[3])
            dicoGraphe[str(x.split()[2])][str(x.split()[1])] = int(x.split()[3])
        if x[:1] == 'V' and x.split()[1] != "num_sommet":
            numLigne = str(x.split(";")[1])
            nomStation = x.split(";")[0].split()
            del nomStation[0]  # Correspond au 'V'
            del nomStation[0]  # Correspond au numéro
            nomSommet[int(x.split()[1])] = ''.join(nomStation) + " ligne " + numLigne


    d = {}
    #d = dictionary(d)
    #print(d)
    matriceArc = np.zeros((376, 376))
    for ligne in lignes:
        if ligne[:1] == 'E' and ligne.split()[1] != "num_sommet1":
            tabLigne = ligne.split();
            matriceArc[int(tabLigne[1])][int(tabLigne[2])] = int(tabLigne[3])

    longueur = dijkstra(dicoGraphe, "256", "288")
    print("Vous devriez arriver dans " + str(round(longueur / 60)) + " minutes. La RATP vous souhaite un bon voyage")
    print(estConnexe(matriceArc, 41))
    ACPM = Kruskal(matriceArc)
    print("len(ACPM) = ", len(ACPM))
    print(ACPM)
    print("somme = ", somme(ACPM))

    #app = Graphes()
    #app.mainloop()
