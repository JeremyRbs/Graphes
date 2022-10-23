#Algo Kruskal vLuc


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

def estCycle(matriceAdj):
    n = len(matriceAdj)
    for i in range(n):
        if ExistChemin(matriceAdj, i, i) == True:
            return True
    return False

def Kruskal(Matrice):
    matriceArc = np.zeros((376, 376))
    file = open("C:\\Users\\lucqu\\PycharmProjects\\graphe\\metro.txt", encoding='utf-8')
    line = file.readlines()
    for ligne in lignes:
        if ligne[:1] == 'E' and ligne.split()[1] != "num_sommet1":
            tabLigne = ligne.split();
            matriceArc[int(tabLigne[1])][int(tabLigne[2])] = int(tabLigne[3])

    for i in range(0,376):
        for j in range(0,376):
            