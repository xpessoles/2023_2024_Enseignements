# -*- coding: utf-8 -*-
import time

from collections import deque
import matplotlib.pyplot as plt
import random


##########TP : partie préliminaire

## Question 1 ##
def creer_graphe(p:int, n:int) -> dict:
    # n : lignes
    # p : colonnes
    G = {}
    sommets = []
    for i in range(n):
        for j in range(p):
            sommets.append((j,i))
    
    for sommet in sommets : 
        (i,j) = sommet
        voisins = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
        # On vérifie que les voisins sont dans les sommets
        vv = []
        for v in voisins : 
            if v in sommets : 
                vv.append(v)
        G[sommet]=vv
    return G

## Question 2 ##
def get_sommets(G:{}) -> ([],[]):
    # On trace les sommets
    les_x,les_y = [],[]
    for sommet in G.keys() : 
        les_x.append(sommet[0])
        les_y.append(sommet[1])
    return les_x,les_y
                
### question 3 ##
def trace_sommets(G:dict,couleur:int)->None:
    les_x,les_y=get_sommets(G)
    plt.plot(les_x,les_y,couleur+'.')
    plt.axis('equal')
 
    
    
## Question 4 ##
def get_aretes(G):
    edges = []
    for sommet,voisins in G.items():
        for v in voisins : 
            edge = [sommet,v]
            if [sommet,v] not in edges : 
                if [v,sommet] not in edges : 
                    edges.append(edge)
    return edges


## Question 5 ##  
def trace_arete(s1,s2,couleur,epaisseur)->None:
    les_x = [s1[0],s2[0]]
    les_y = [s1[1],s2[1]]
    plt.plot(les_x,les_y,couleur,linewidth=epaisseur)
    
    

## Question 6 ##
def trace_graphe(G:dict,couleur:str,epaisseur:int)->None:
    aretes=get_aretes(G)
    for a in aretes :
        trace_arete(a[0],a[1],couleur,epaisseur)
    trace_sommets(G,couleur)

plt.figure("Activité prépa")
G=creer_graphe(10,8)
trace_graphe(G,'r',1)

##########TP

##Question 1
def ajouter_arete(L,s1,s2):
    '''ajoute l'arrete (s1,s2) au graphe L, si elle n'existe pas déjà'''
    if (s1 not in L.keys()) :  # si s1 n'existe pas
        L[s1]=[s2]
    if (s2 not in L.keys()):
        L[s2]=[s1]

    if s2 not in L[s1] : #si s2 n'est pas dans les voisins de s1
         L[s1].append(s2)
    if s1 not in L[s2] :
         L[s2].append(s1)

         
G2=creer_graphe(2,2)
ajouter_arete(G2,(1,0),(2,0))


G=creer_graphe(10,10)


##Question 2 
G=creer_graphe(5,5)

plt.figure("Tests tracés")
trace_graphe(G,'r',1)

##Question 3
visited = {}
for sommet in G.keys():
    visited[sommet] = 'W'
    
##Question 4
def trace_visites(v:dict):
    for e in v.keys():
        if v[e]=='G':
            plt.plot(e[0],e[1],'o',color='grey',markersize=8)  #Tracé des éléments visités en gris
        if v[e]=='K':
            plt.plot(e[0],e[1],'ko',markersize=8)  #Tracé des éléments explorés en noir



##Question 5
visited[(2,1)]='G'
visited[(4,1)]='G'
visited[(3,1)]='G'
visited[(3,2)]='K'
trace_visites(visited)

##Question 6 (abandonnée)   
# def trace_file(f):
#     if len(f)>0:
#         for e in f:
#             plt.plot(e[0],e[1],'bx',markersize=8)    #Tracé des éléments de la file avec des marqueurs en croix bleue
#         e=f[-1]
#         plt.plot(e[0],e[1],'bx',markersize=16)    #ajout d'une croix plus grosse pour la tête de file

##Question 7  
# file=deque([(1,0),(2,1),(4,3)])
# trace_file(file)
# print(file)

##Question 8    
# def trace_etat(G : dict,v : dict,f : list)->None :
#     #plt.clf()
#     #trace_file(f)
#     #trace_graphe(G,'r',1)
#     trace_visites(v)
#     
##Question 6 : initialisation
def parcours_largeur_init(G:{},depart:tuple) :
    
    visited = {}
    for sommet in G.keys():
        visited[sommet] = 'W'
    
    visited[depart]='G' #le premier sommet est vu
    file = deque([depart])
    trace_visites(visited)
    

plt.figure("largeur_initial")
parcours_largeur_init(G,(2,0))

##Question 7 : parcours en largeur : etape 1
def parcours_largeur_etape1(G:{},depart:tuple) :
    
    visited = {}
    for sommet in G.keys():
        visited[sommet] = 'W'
    
    visited[depart]= 'G' #le premier sommet est vu
    
    file = deque([depart])
    
    s=file.pop()
    voisins = G[s]
    
    for v in voisins:
        if visited[v]=='W' : #voisins non découverts
            file.appendleft(v)   #ajout dans la file des voisins non visités
            visited[v]='G'
    visited[s]='K'
    trace_visites(visited)
    
plt.figure("largeur_étape1")
trace_graphe(G,'r',1)
parcours_largeur_etape1(G,(0,0))
#plt.show()

##Question 8 : parcours en largeur complet
def parcours_largeur_complet(G:{},depart: tuple) :
    visited = {}
    for sommet in G.keys():
        visited[sommet] = 'W'
    
    visited[depart]='G' #le premier sommet est vu
    file = deque([depart])
    
    while len(file) > 0:
        s = file.pop()
      
        voisins = G[s]
        random.shuffle(voisins)
        
        for v in voisins:
                if visited[v]=='W' : #voisins non découverts
                    file.appendleft(v)   #ajout dans la file des voisins non visités
                    trace_arete(s,v,'k',3)
                    visited[v]='G' #ce voisin a été vu
        visited[s]='K'
        
        plt.pause(0.3)
        #print(file)
        trace_visites(visited)
    
G=creer_graphe(10,10)
#Animation (parcours en largeur)
#plt.figure("largeur")

#trace_graphe(G,'r',1)
#parcours_largeur_complet(G,(0,0))

##Question 9 : génération du labyrinthe avec parcours largeur
def labyrinthe_largeur(G:{},depart:tuple) :
    labyrinthe={}
    
    visited = {}
    for sommet in G.keys():
        visited[sommet] = 'W'
    
    visited[depart]='G' #le premier sommet est vu
    file = deque([depart])
    
    while len(file) > 0:
        s = file.pop()
      
        voisins = G[s]
        random.shuffle(voisins)
        
        for v in voisins:
                if visited[v]=='W' : #voisins non découverts
                    file.appendleft(v)   #ajout dans la file des voisins non visités
                    ajouter_arete(labyrinthe, s, v)
                    visited[v]='G' #ce voisin a été découvert
        visited[s]='K'
        
        #trace_graphe(labyrinthe,'k',3)
        #plt.pause(0.3)
    return(labyrinthe)
    
    
L=labyrinthe_largeur(G,(0,0))
plt.figure('labyrinthe en largeur')
trace_graphe(G,'r',1)
trace_graphe(L,'k',3)

##Question 10 : parcours en profondeur
def parcours_profondeur(G:{},depart:tuple) :
    visited = {}
    
    for sommet in G.keys():
        visited[sommet] = 'W'

    pile = deque([depart])
    visited[depart]='G'

    while len(pile) > 0:
        trace_visites(visited)
        
        s = pile[-1]
        voisins_blanc=[v for v in G[s] if visited[v]=='W']
        random.shuffle(voisins_blanc)
        
        if voisins_blanc:  #il y a encore des voisins non découverts
            v=voisins_blanc[0]
            trace_arete(s,v,'k',3)
            visited[v]='G'
            pile.append(v)
        
        else: #si plus de voisins blancs
            s=pile.pop()
            visited[s]='K'
        
        plt.pause(0.3)
        
#Animation (parcours en profondeur)
#plt.figure("parcours en profondeur")
#trace_graphe(G,'r',1)
#parcours_profondeur(G,(0,0))
   
   
##Question 11 :  labyrinthe parcours en profondeur
def labyrinthe_profondeur(G:{},depart:tuple) :
    visited = {}
    laby={}
    
    for sommet in G.keys():
        visited[sommet] = 'W'

    pile = deque([depart])
    visited[depart]='G'

    while len(pile) > 0:
        
        s = pile[-1]
        voisins_blanc=[v for v in G[s] if visited[v]=='W']
        random.shuffle(voisins_blanc)
        
        if voisins_blanc:  #il y a encore des voisins non découverts
            v=voisins_blanc[0]
            ajouter_arete(laby,s,v)
            visited[v]='G'
            pile.append(v)
        
        else: #si plus de voisins blancs
            s=pile.pop()
            #visited[s]='K'
        
        #trace_graphe(laby,'k',4)
        #trace_visites(visited)
        #plt.pause(0.3)
        
    return(laby)    



t1=time.perf_counter()
L=labyrinthe_profondeur(G,(0,0))
t2=time.perf_counter()
dt1=t2-t1

plt.figure("labyrinthe en profondeur")
trace_graphe(G,'r',1)
trace_graphe(L,'k',2)

# def labyrinthe_profondeur_ancienneversion(G,depart) :
#     labyrinthe = {}
#     predecesseurs = {}
# 
#     for sommet in G.keys():
#         predecesseurs[sommet] = False
# 
#     
#     pile = deque([(depart,depart)])
# 
#     while len(pile) > 0:
#         s1,s2 = pile.pop()
#         if predecesseurs[s1] == False:
#             predecesseurs[s1] = s2
#             voisins = G[s1]
#             random.shuffle(voisins)
#             for v in voisins:
#                 pile.append((v,s1))
#             ajouter_arete(labyrinthe, s1, s2)
#             #trace_graphe(labyrinthe)
#             #plt.pause(0.3)
#     return labyrinthe
# 
# t1=time.perf_counter()
# L=labyrinthe_profondeur_ancienneversion(G4,(0,0))
# t2=time.perf_counter()
# dt2=t2-t1
#plt.figure("labyrinthe en profondeur_ancien")
#trace_graphe(G,'r',1)
#trace_graphe(L,'k',2)

##Partie 5 : résolution du labyrinthe
def resolution_largeur(G:{},depart:tuple,arrivee:tuple):
    
    labyrinthe={}
    
    visited = {}
    for sommet in G.keys():
        visited[sommet] = 'W'
    
    visited[depart]='G' 
    file = deque([depart])
    
    while len(file) > 0:
        s = file.pop()
      
        voisins = G[s]
        for v in voisins:
                if visited[v]=='W' : #voisins non découverts
                    file.appendleft(v)   #ajout dans la file des voisins non visités
                    visited[v]=s #ce voisin a été découvert, on stocke son predecesseur
    
    chemin=remontee(visited,arrivee)
                    
    return(chemin)

def resolution_profondeur(G:{},depart:tuple,arrivee:tuple) :
    visited = {}
    
    for sommet in G.keys():
        visited[sommet] = 'W'

    pile = deque([depart])
    visited[depart]='G'

    while len(pile) > 0:
        
        s = pile[-1]
        voisins_blanc=[v for v in G[s] if visited[v]=='W']
        
        if voisins_blanc:  #il y a encore des voisins non découverts
            v=voisins_blanc[0]
            visited[v]=s  # on stocke son predecesseur et marque comme découvert
            pile.append(v)
        
        else: #si plus de voisins blancs
            s=pile.pop()
    
    chemin=remontee(visited,arrivee)
    return(chemin)    


def remontee(parcours:{},s:tuple):
    '''remonte le dictionnaire des predecesseurs parcours à partir de s'''
    chemin=[s]
    p=s
    while p!=(0,0):
        p=parcours[s]
        chemin.append(p)
        s=p
    return(chemin)

G5=creer_graphe(10,10)
lab=labyrinthe_profondeur(G5,(0,0))  #création du labyrinthe
chemin1= resolution_largeur(lab,(0,0),(9,9)) #parcours en largeur du labyrinthe
chemin2= resolution_profondeur(lab,(0,0),(9,9)) #parcours en profondeur du labyrinthe


#Trace
plt.figure("resolution")    
trace_graphe(lab,'k',2) #tracé du labyrinthe

#trace du chemin
chemin=chemin2
for i in range(len(chemin)-1):
    trace_arete(chemin[i],chemin[i+1],'b',4)


plt.show()