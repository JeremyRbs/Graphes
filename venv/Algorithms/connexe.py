# Méthode permettant de vérifier si le graphe fourni est connexe
def estConnexe(matrice, pointDep):

    n = len(matrice)  # nombre de sommets dans le graphe
    tabVisite = [];     # tableau des sommets visités
    file = [pointDep];

    # Tant que des points existent
    while file:
        current = file.pop(0)
        tabVisite.append(current);
        for i in range(n):
            if i != current and (matrice[current][i] > 0 or matrice[i][current] > 0) and i not in tabVisite:
                file.append(i);
        if len(tabVisite) == n:
            return True
    return False