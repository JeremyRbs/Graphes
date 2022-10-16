

from collections import deque

def dictionary(d):
    file = open("C:\\Users\\jerem\\PycharmProjects\\Graphes\\venv\\Data\\metro.txt", encoding='utf-8')
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