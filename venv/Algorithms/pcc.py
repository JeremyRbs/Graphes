

from collections import deque


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

