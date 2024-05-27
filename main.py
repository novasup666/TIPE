import queue as q

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
        if self.weight(x,y) == 0:
            self.adj[x].append(y)
        self.matrix[x][y] += w

    def update_edge(self,x,y,v):
        assert(self.weight(x,y)!=0)
        if v == 0:
            self.adj[x].remove(y)
        if v>0:
            self.matrix[x][y] = v
        else:
            self.matrix[y][x] = -v
            
    def edges(self,x):
        return [(y, self.weight(x,y)) for y in self.adj[x]]
    
    def custom_copy(self):
        g = graph.init(self.size)
        g.matrix = [t.copy() for t in self.matrix]
        g.adj = [t.copy() for t in self.adj]
        g.s = self.s
        g.t = self.t
        return g   

DATA = [('s',0,4),('s',2,4),('s',2,3),('s',3,4),('s',4,4),('s',5,3),('s',6,3),('s',7,7),('s',8,3),('s',9,2),('s',10,2),(0,1000,3),(1,11,5),(1,45,5),(2,45,5),(45,44,5),(44,43,5),(43,41,5),(2,3,4),(3,4,4),(4,5,4),(5,42,4),(41,42,4),(42,6,4),(41,40,5),(40,46,2),(46,38,6),(38,37,6),(6,37, 5),(6,36,5),(37,36,5),(7,36,7),(36,39,12),(38,39,3),(39,1001,12),(39,20,4),(36,35,3),(35,34,3),(19,34,3),(8,19,6),(19,23,1),(24,23,4),(18,24,3),(23,25,3),(23,27,4),(27,29,4),(29,21,4),(20,21,11),(21,54,3),(54,55,3),(25,31,4),(31,32,4),(25,26,5),(26,28,5),(29,28,4),(28,30,4),(30,33,3),(28,22,4),(21,22,7),(22,33,7),(33,1002,8),(51,33,7),(53,51,2),(52,53,2),(52,49,5),(55,52,2),(54,49,3),(49,51,3),(22,49,5),(10,12,5),(10,9,5),(9,16,4),(12,15,4),(12,11,5),(15,17,3), (16,17,5),(16,18,3),(17,18,4) ]

Vertices = set.union({x for x,_,_ in DATA},{x for _,x,_ in DATA})
N = len(Vertices)

def rebuild_path(g,partial, start,end):
    path = []
    current = end
    treated = set()
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
    partial[node] = float("inf")
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
    return widest_path

def init_ag(g,sinks) : 
    """
    Construit le graphe des augmentations
    Builds the augmenting graph

    On ajoutera des arcs de capacités infinies entre t (un noeud virtuel) et les differents points de sorties réels
    We will add to ag edges of infinite capacity between t (a virtual sink node) and the different real sink nodes
    """
    n = g.size
    ag = g.custom_copy()
    ag.matrix = [row for row in ag.matrix]
    ag.matrix.append([0 for _ in range ( n +1)])
    g.size = n+1
    g.t = n
    for s in sinks:
        ag.add_edge (s,g.t, float("inf"))
    return ag

def update_ag(ag,ap,dphi):
    """
    Met le graphe des augmentations à jour en soustrayant aux aretes du chemin augmentant
    considéré le supplément de flux.
    Updates the augmenting graph regarding the evolution dphi of flux.
    Pour chaque arete emprunté la capacité restante est réduite de dphi et la capacité restante de l'arc inverse est augmentée de 1
    """
    n = len(ap)
    ag.update(x, y, ag.weight(ap[0],ap[1])-dphi)
    for i in range(2,n-1):
        x = ap[i-1]
        y = ap[i]
        ag.update_edge(x, y, ag.weight(x,y)-dphi)
        ag.update_edge(y, x, ag.weight(x,y)+dphi)
        
def init_flow(g):
    return graph.init(g.size)

def update_flow(f,ap,dphi):
    n = len(ap)
    for i in range(1,n-1):
        x = ap[i-1]
        y = ap[i]
        f_inverse = f.weight(y,x)
        diff = dphi - f_inverse
        f.update_edge(x,y,diff)

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
        dphi = partial[current]
        aretes = ag.edges(current)
        vus.add(current)
        for y,w in aretes:
            if y not in vus:
                bag.put(y)
                partial[y] = (current,min(w,dphi))
    if partial[ag.t] != -1 :
        return (True,rebuild_path(ag,partial,ag.s,ag.t),partial[ag.t][1])
    else:
        return (False, None)

def edmond_karp(g, sinks):
    ag = init_ag(g,sinks)
    (found,ap,dphi) = find_path(ag)
    f = init_flow(ag)
    while found:
        update_ag(ag,ap,dphi)
        update_flow(f,ap)
        (ap,found) = find_path(ag)
    return f 


def main():
    """
    rep et sigma permettent de traiter les trous dans la numérotation des noeuds et l'utilisation de s
    simplifie la vie.
    """

    print("--------------------------------\nCeasefire for Palestine\n")
    g = graph(N)
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
    fin = 40
    g.t = None
    rho = {v:k for (k,v) in sigma.items()}    
    p = widest_path(g,sigma["s"],sigma[fin])
    print("The widest path between s and {fin}")
    print([rho[e] for e in p])
    
main()

