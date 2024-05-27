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
