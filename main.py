import queue as q
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

DATA = [('s',0,4),('s',2,4),('s',2,3),('s',3,4),('s',4,4),('s',5,3),('s',6,3),('s',7,7),('s',8,3),('s',9,2),('s',10,2),(0,1000,3),(1,11,5),(1,45,5),(2,45,5),(45,44,5),(44,43,5),(43,41,5),(2,3,4),(3,4,4),(4,5,4),(5,42,4),(41,42,4),(42,6,4),(41,40,5),(40,46,2),(46,38,6),(38,37,6),(6,37, 5),(6,36,5),(37,36,5),(7,36,7),(36,39,12),(38,39,3),(3,44,1),(39,1001,12),(39,20,4),(36,35,3),(35,34,3),(19,34,3),(8,19,6),(19,23,1),(24,23,4),(18,24,3),(23,25,3),(23,27,4),(27,29,4),(29,21,4),(20,21,11),(21,54,3),(54,55,3),(25,31,4),(31,32,4),(25,26,5),(26,28,5),(29,28,4),(28,30,4),(30,33,3),(28,22,4),(21,22,7),(22,33,7),(33,1002,8),(51,33,7),(53,51,2),(52,53,2),(52,49,5),(55,52,2),(54,49,3),(49,51,3),(22,49,5),(10,12,5),(10,9,5),(9,16,4),(12,15,4),(12,11,5),(15,17,3), (16,17,5),(16,18,3),(17,18,4), (34,20,4),(61,58,3),(58,57,3),(60,59,3),(59,56,3),(55,56,3),(56,57,4),(59,58,1),(59,52,4),(61,60,3),(60,53,3) ]
Positions = [(0, 89, 238), (1, 113, 165), (2, 174, 104), (3, 206, 95), (4, 235, 95), (5, 262, 94), (6, 271, 132), (7, 302, 155), (8, 277, 251), (9, 158, 249), (10, 141, 244), (11, 116, 206), (12, 127, 253), (15, 118, 271), (16, 164, 267), (17, 143, 272), (18, 159, 289), (19, 309, 253), (20, 435, 242), (21, 437, 265), (22, 437, 325), (23, 334, 273), (24, 301, 276), (25, 339, 335), (26, 369, 331), (27, 367, 268), (28, 400, 328), (29, 396, 269), (30, 400, 383), (31, 343, 392), (32, 298, 401), (33, 437, 378), (34, 378, 246), (35, 357, 209), (36, 329, 161), (37, 327, 133), (38, 336, 92), (39, 382, 156), (40, 289, 39), (41, 269, 48), (42, 274, 94), (43, 231, 62), (44, 205, 71), (45, 175, 86), (46, 321, 59), (49, 471, 322), (51, 473, 374), (52, 497, 320), (53, 499, 371), (54, 467, 264), (55, 494, 260), (56, 515, 260), (57, 534, 259), (58, 535, 320), (59, 518, 319), (60, 519, 369), (61, 538, 367), ('s', 210, 197), (1000, 40, 284), (1001, 443, 146), (1002, 452, 418)]

def find(i, pos):
    if i not in rho:
        return (0,i)
    else:
        i = rho[i]
        for j in range(len(pos)):
            if i == pos[j][0]:
                return (pos[j][1], -pos[j][2])
        return (0,i)

def show_graph_with_labels(adjacency_matrix, mylabels,path = [],w = 0):
    """ 
        La fonction utilise [0; |V|] comme ensemble de sommets (pas le mélange chaine de caractère, entier non consecutif)
        This function uses [0; |V|] as vertices set (not the strings, nonconsecutive integer mix)
    """
    G = nx.from_numpy_array(adjacency_matrix, parallel_edges=True, create_using=nx.Graph)
    ly= {i:find(i,Positions) for i in range(len(adjacency_matrix))}
    #nx.draw_networkx_edge_labels(G,pos=ly)
    N = len(adjacency_matrix)
    path_edges = {(path[i-1],path[i]) for i in range(1,len(path))}
    couleurs = ['k' if (u,v) not in path_edges and (v,u) not in path_edges else "red" for u,v in G.edges()]
    for u,v in path_edges:
        G[u][v]['weight'] = w
    poids = [G[u][v]['weight'] for u,v in G.edges()]

    nx.draw_networkx_edges(G,pos=ly)
    nx.draw_networkx(G, node_size=700, labels=mylabels, with_labels=True, 
                     pos=ly, width = poids, edge_color = couleurs )
    plt.show()

def show_example(adjacency_matrix, path = [], w = 0):
    G = nx.from_numpy_array(adjacency_matrix, parallel_edges=True, create_using=nx.DiGraph)
    ly= {0:(0,0),1:(2,1),2:(2,-1),3:(4,0),4:(6,1),5:(6,-1),6:(8,0)}
    #nx.draw_networkx_edge_labels(G,pos=ly)
    N = len(adjacency_matrix)
    mylabels = {i:i for i in range (N)}
    path_edges = {(path[i-1],path[i]) for i in range(1,len(path))}
    couleurs = ['k' if (u,v) not in path_edges and (v,u) not in path_edges else "red" for u,v in G.edges()]
    for u,v in path_edges:
        G[u][v]['weight'] = str(w)/G[u][v]['weight']
    poids = {(u,v): str (G[u][v]['weight']) for u,v in G.edges()}

    nx.draw_networkx_edges(G,pos=ly)
    nx.draw_networkx_edge_labels(G,pos = ly, edge_labels=poids, font_color='b', font_size=15)
    nx.draw_networkx(G, node_size=700, labels=mylabels, with_labels=True, 
                     pos=ly, edge_color = couleurs, arrowsize = 20 )
    plt.show()  



class max_heap:
    """
    Une implementation personnelle d'un tas max stockant des tuples (int, any)
    basé sur un arbre linéarisé dans un tableau (ici une liste).

    A custom implementing of max heap to store tuples (int, any) 
    based on a linearised tree (a list).
    """
    def __init__(self) -> None:
        self.data = []
        self.size = 0


    def switch(self,i1,i2):
        assert(0 <= i1 < self.size)
        assert(0 <= i2 < self.size)
        tmp = self.data[i1]
        self.data[i1] = self.data[i2]
        self.data[i2] = tmp


    def sift_up (self,index):
        k = index
        k_prime = int((k-1)/2)
        p = self.data[k][0]
        while self.data[k_prime][0] < p:
            self.switch(k,k_prime)
            k = k_prime
            k_prime = int((k-1)/2)

    def sift_down(self,index):
        k = index
        k_prime = k
        if 2*k+1 < self.size and self.data[2*k+1][0] > self.data[k_prime][0]:
            k_prime = 2*k+1 
        if 2*k+2 < self.size and self.data[2*k+2][0] > self.data[k_prime][0]:
            k_prime = 2*k+2
        while k!=k_prime:
            self.switch(k,k_prime)
            k = k_prime
            if 2*k+1 < self.size and self.data[2*k+1][0] > self.data[k_prime][0]:
                k_prime = 2*k+1 
            if 2*k+2 < self.size and self.data[2*k+2][0] > self.data[k_prime][0]:
                k_prime = 2*k+2


    def push(self, p,v):
        self.data.append((p,v))
        self.size += 1
        self.sift_up(self.size-1)
    
    def pop (self):
        if self.size > 1:        
            self.switch(0, self.size-1)
        res = self.data.pop()
        self.size-=1
        self.sift_down(0)
        return res

class graph:
    def __init__(self,n) -> None:
        self.size = n
        self.matrix = [[0 for _ in range(n)] for _ in range (n)]
        self.adj = [[]for _ in range(n)]
        self.s = -1
        self.t = -1

    def weight(self,x,y):
        return self.matrix[x][y]
    
    def add_edge(self,x,y,w):
        # directed edges
        assert(w!=0)
        if self.weight(x,y) == 0:
            self.adj[x].append(y)
        self.matrix[x][y] += w

    def update_edge(self,x,y,v):
        if v == 0:
            self.matrix[x][y] = v
            self.adj[x].remove(y)
        if v>0:
            self.matrix[x][y] = v
        else:
            self.matrix[y][x] = -v
            
    def edges(self,x):
        return [(y, self.weight(x,y)) for y in self.adj[x]]
    
    def custom_copy(self):
        g = graph(self.size)
        g.matrix = [t.copy() for t in self.matrix]
        g.adj = [t.copy() for t in self.adj]
        g.s = self.s
        g.t = self.t
        return g   



Vertices = set.union({x for x,_,_ in DATA},{x for _,x,_ in DATA})
N = len(Vertices)

def rebuild_path(g,partial, start,end):
    path = []
    current = end
    while current !=  start :
        next = partial[current][0]
        path.append(next)
        current = next
    path.reverse()
    path.append(end)
    return path

def widest_path (g, start, end):
    """
    Version adaptée de Dijkstra au probleme considéré : chemin le plus
    large: maximum des minimum des capacités des arètes.

    Adapted implementation of Dijkstra's algorithm to solve the
    widest-path problem: looking for the paht with the biggest of 
    minimum capacity along its way.
    """
    node =  start
    bag = max_heap()
    bag.push(float("inf"),node)
    partial = [(-1,0) for _ in range(g.size)]
    partial[node] = (float("inf"), node)
    treated = set()
    while end not in treated: 
        (capa,node) = bag.pop()
        treated.add(node)
        edges = g.edges(node)
        for (y,w) in edges:
            new_capa = min(capa,w)
            if y not in treated and ( partial[y][1] == 0  or new_capa > partial[y][1]):
                bag.push(new_capa,y)
                partial[y] = (node,new_capa) # garder node permet de se souvenir du meilleur père et de simplifier rebuild_path


    widest_path = rebuild_path (g, partial, start, end)
    return (widest_path, partial[end][1])

def init_ag(g,sinks) : 
    """
    Construit le graphe des augmentations
    Builds the augmenting graph

    On ajoutera des arcs de capacités infinies entre t (un noeud virtuel) et les differents points de sorties réels
    We will add to ag edges of infinite capacity between t (a virtual sink node) and the different real sink nodes
    """
    if sinks != None:
        n = g.size
        ag = g.custom_copy()
        ag.matrix = [row+[0] for row in ag.matrix]
        ag.matrix.append([0 for _ in range(n +1)])
        ag.adj.append([])
        ag.size = n+1
        ag.t = n
        ag.s = g.s
        for s in sinks:
            ag.add_edge (s,ag.t, float("inf"))
    else:
        ag = g.custom_copy()
    return ag

def update_ag(ag,ap,dphi):
    """
    Met le graphe des augmentations à jour en soustrayant aux aretes du chemin augmentant
    considéré le supplément de flux.
    Updates the augmenting graph regarding the evolution dphi of flux.
    Pour chaque arete emprunté la capacité restante est réduite de dphi et la capacité restante de l'arc inverse est augmentée de 1
    """
    n = len(ap)

    for i in range(1,n):
        x = ap[i-1]
        y = ap[i]
        ag.update_edge(x, y, ag.weight(x,y)-dphi)
        ag.update_edge(y, x, ag.weight(y,x)+dphi)
    
        
def init_flow(g):
    return graph(g.size)

def update_flow(f,ap,dphi):
    n = len(ap)
    for i in range(1,n):
        x = ap[i-1]
        y = ap[i]
        f_inverse = f.weight(y,x)
        diff = dphi - f_inverse
        f.add_edge(x,y,diff)

def find_path(ag):
    """
    Cherche et (parfois) trouve le chemin augmentant le plus court pour le flot dans ag

    Renvoie (b,ap,dphi)
    -b; booleen indiquant si un chemin augmentant pour le flux à été trouvé
    -ap: edge list le chemin, [] si n'existe pas.

    On considère le poids de chaque rue comme unitaire 

    Looks for and (sometime) finds the shortest augmenting path for the flux in the augmenting graph

    Returns (b,ap,dphi):
    - b: boolean indicating wheter or not the augmenting path has been found.
    - ap: edge (int) list, the path itself
    - dphi: int :  the change of flux

    """
    bag = q.Queue()
    bag.put(ag.s)
    dphi = float("inf")
    vus = set()
    partial = [(-1,float('inf')) for _ in range(ag.size)]
    while not bag.empty():
        current = bag.get()
        dphi = partial[current][1]
        aretes = ag.edges(current)
        vus.add(current)
        for y,w in aretes:
            if y not in vus:
                bag.put(y)
                partial[y] = (current,min(w,dphi))
    if partial[ag.t][0] != -1 :
        return (True,rebuild_path(ag,partial,ag.s,ag.t),partial[ag.t][1])
    else:
        return (False, None, 0)
def printmat(m):
    for r in m : print(r,"\n")


def edmond_karp(g, sinks):
    ag = init_ag(g,sinks)
    (found,ap,dphi) = find_path(ag)
    f = init_flow(ag)
    show_example(np.matrix(f.matrix))
    while found:
        update_ag(ag,ap,dphi)
        update_flow(f,ap,dphi)
        (found,ap,dphi) = find_path(ag)
        show_example(np.matrix(ag.matrix,ap,dphi))
        show_example(np.matrix(f.matrix))
    return f 



def main():
    """
    rep et sigma permettent de traiter les trous dans la numérotation des noeuds et l'utilisation de s
    simplifie la vie.
    """

    print("--------------------------------\nCeasefire for Palestine\n")
    g = graph(N)
    global sigma
    sigma = {}
    i = 0
    for v in Vertices:
        sigma[v] = i
        i+=1
    for i in range(len(DATA)):
        x,y,w = DATA[i]
        rx = sigma[x]
        ry = sigma[y]
        g.add_edge(rx,ry,w)
        g.add_edge(ry,rx,w)
    g.s = sigma["s"]
    fin = 1002
    g.t = None
    global rho
    rho = {v:k for (k,v) in sigma.items()}    

    p,w = widest_path(g,sigma["s"],sigma[fin])
    print(f"The widest path between s and {fin}")
    print([rho[e] for e in p])

    """
    f = edmond_karp(g,[sigma[1001],sigma[1000], sigma[1002]])
    
    #show_graph_with_labels(np.matrix(g.matrix),rho)
    show_graph_with_labels(np.matrix(g.matrix),rho, p,w)
    print("\nw:",w)
    #show_graph_with_labels(np.matrix([r[0:-1] for r in f.matrix][0:-1]),rho)
    """
    ex = graph(7)
    ex.matrix = [
        [0,5,15,0,0,0,0],
        [0,0,0,0,7,0,0],
        [0,0,0,3,0,12,0],
        [0,6,0,0,0,0,2],
        [0,0,0,0,0,0,8],
        [0,0,0,5,0,0,5],
        [0,0,0,0,0,0,0],                
    ]
    ex.adj = [
        [1,2],
        [4],
        [3,5],
        [1,6],
        [6],
        [3,6],
        []
    ]
    ex.s = 0;
    ex.t = 6;
    f = edmond_karp(ex,None)
    #show_example(np.matrix(ex.matrix))
    #"""
main()

