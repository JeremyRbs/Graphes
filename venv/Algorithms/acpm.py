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

def nappartient_pas_a_T(j,T):
    for i in range(len(T)):
        if(j == T[i]):
            return false
    return true

def Kruskal(Matrice):
    copie_matrice = Matrice
    matrice_obtenu = np.zeros((376, 376))
    min = {"poids":0,"sommet_dorigine":0,"sommet_darrive":0};
    T = list(char);
    
    while(len(T)<376):
        for i in range(0,376):
            for j in range(0,376):
                if(copie_matrice[i][j] != 0):
                    if(copie_matrice[i][j] < min["poids"] and nappartient_pas_a_T(j,T) and not estCycle(matrice_obtenu, i, j)):
                        min["poids"] = copie_matrice[i][j]
                        min["sommet_dorigine"] = i
                        min["sommet_darrive"] = j
                        matrice_obtenu[i][j] = copie_matrice[i][j]
                        copie_matrice[i][j] = 0
                        if (len(T) == 0):
                            T.append(i)
                        T.append(j)
    return T



