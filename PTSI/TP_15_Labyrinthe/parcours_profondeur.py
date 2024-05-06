def parcours_profondeur(G,depart) :
    visited = {}

    for sommet in G.keys():
        visited[sommet] = False

    pile = deque([depart])
    visited[depart]= True

    while len(pile) > 0:

        s = pile[-1]
        L=[v for v in G[s] if visited[v]==False]

        if L:
            v=L[0]
            visited[v]=True
            pile.append(v)

        else :
            s=pile.pop()
