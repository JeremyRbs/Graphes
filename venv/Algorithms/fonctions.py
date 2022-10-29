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


def nappartient_pas_a_T(i,j, T):
    for k in range(len(T)):
        if (j == T[k]["sommet_darrive"] and i == T[k]["sommet_dorigine"]):
            return False
    return True

def nappartient_pas_a_V(i,j, V):
    for k in range(len(V)):
        if(j == V[k]["sommet_darrive"] and i == V[k]["sommet_dorigine"]):
            return False
    return True

def afficher_list(list):
    for i in range(len(list)):
        print("list[",i,"] = ", list[i])