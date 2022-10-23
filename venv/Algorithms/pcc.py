

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


print(estConnexe(matriceArc, 41))

def dictionary(d):
    file = open("C:\\Users\\lucqu\\PycharmProjects\\graphe\\metro.txt", encoding='utf-8')
    line = file.readlines()

    for x in line:
        if x[:1] == 'E' and x.split()[1] != "num_sommet1":
            d[str(x.split()[1])] = {}

    for x in line:
        if x[:1] == 'E' and x.split()[1] != "num_sommet1":
            d[str(x.split()[1])][str(x.split()[2])] = int(x.split()[3])

    return d

def dijkstra(graph, vertex):
    queue = deque([vertex])
    distance = {vertex: 0}
    while queue:
        t = queue.popleft()
        print("On visite le sommet " + str(t))
        for voisin in graph[t]:
            if voisin in graph:
                queue.append(voisin)
                nouvelle_distance = distance[t] + graph[t][voisin]
                if (voisin not in distance or nouvelle_distance < distance[voisin]):
                    distance[voisin] = nouvelle_distance
                    print("Met à jour le sommet " + str(voisin) + " avec la distance : " + str(nouvelle_distance))
            else:
                print("C'est un terminus le sommet ", voisin, " poto ...")

    return distance


# Liste d'ajacence du graphe
graph = {}
graph = dictionary(graph)
print(graph)
#distance = dijkstra(graph, '0')
#print("Distances" + str(distance))