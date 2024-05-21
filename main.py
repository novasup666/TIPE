

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
    def __init__(self,n,source,puit) -> None:
        self.size = n
        self.matrix = [[0 for _ in range(n)] for _ in range (n)]
        self.adj = []
        self.s = source
        self.t = puit
    def weight(self,x,y):
        return self.matrix[x][y]
    
    def add_edge(self,x,y,w):
        if self.weight(x,y) == 0:
            self.adj[x].append(y)
        self.matrix[x][y] = w

    def update_edge(self,x,y,v):
        assert(self.weight(x,y)!=0)
        if v == 0:
            self.adj[x].remove(y)
        self.matrix[x][y] = v

    def edges(self,x):
        return [(y, self.weight(x,y)) for y in self.adj[x]]
    
    def custom_copy(self):
        g = graph.init(self.size)
        g.matrix = [t.copy() for t in self.matrix]
        g.adj = [t.copy() for t in self.adj]
        return g
    


    

DATA = [('s',0,4),('s',2,4),('s',2,3),('s',3,4),('s',4,4),('s',5,3),('s',6,3),('s',7,7),('s',8,3),('s',9,2),('s',10,2),(0,1000,3),(1,11,5),(1,45,5),(2,45,5),(45,44,5),(44,43,5),(43,41,5),(2,3,4),(3,4,4),(4,5,4),(5,42,4),(41,42,4),(42,6,4),(41,40,5),(40,46,2),(46,38,6),(38,37,6),(6,37, 5),(6,36,5),(37,36,5),(7,36,7),(36,39,12),(38,39,3),(39,1001,12),(39,20,4),(36,35,3),(35,34,3),(19,34,3),(8,19,6),(19,23,1),(24,23,4),(18,24,3),(23,25,3),(23,27,4),(27,29,4),(29,21,4),(20,21,11),(21,54,3),(54,55,3),(25,31,4),(31,32,4),(25,26,5),(26,28,5),(29,28,4),(28,30,4),(30,33,3),(28,22,4),(21,22,7),(22,33,7),(33,1002,8),(51,33,7),(53,51,2),(52,53,2),(52,49,5),(55,52,2),(54,49,3),(49,51,3),(22,49,5),(10,12,5),(10,9,5),(9,16,4),(12,15,4),(12,11,5),(15,17,3), (16,17,5),(16,18,3),(17,18,4) ]
N = len(DATA)

def rebuild_path(g,partial, start,end):
    path = []
    current = end
    treated = set()
    while current !=  start :
        treated.add(current)
        path.append(current)
        neighbours = g.edges(current)
        candidates = []
        for y,w in neighbours:
            if y not in treated and y in partial:
                candidates.append((min(w,partial[y]),y))
        _,next=max(candidates)
        current = next
    path.append(start)
    path.reverse()
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
    partial = {}
    partial[node] = float("inf")
    treated = set()
    while end not in treated: 
        (capa,node) = bag.pop()
        treated.add(node)
        edges = g.edges(node)
        for (y,w) in edges:
            new_capa = min(capa,w)
            if y not in treated and ( y not in partial or new_capa > partial[y]):
                bag.push(new_capa,y)
                partial[y] = new_capa

    widest_path = rebuild_path (g, partial, start, end)
    return widest_path

def init_ag(g) : 
    """
    Construit le graphe des augmentations
    """
    return g.custom_copy()

def update_ag(ag,ap):
    """
    Met le graphe des augmentations à jour en soustrayant aux aretes du chemin augmentant
    considéré le supplément de flux.
    """
    for(x,y,dphi) in ap:
        ag.update(x, y, ag.weight(x,y)-dphi)



def init_flow(g):
    return graph.init(g.size)

def update_flow(f,p):
    for (x,y,dphi) in p:
        f.update(x, y, f.weight(x,y)+dphi)

def find_path(ag):
    """
    Cherche et (parfois) trouve un chemin augmentant pour le flot dans ag

    Renvoie (b,ap)
    -b indiquant si un chemin augmentant pour le flux à été trouvé
    -ap le chemin, [] si n'existe pas.

    """




def edmond_karp(g, source, puit):
    ag = init_ag(g,source,puit)
    (ap,found) = find_path(ag)
    while found:
        update_ag(ag,ap)
        update_flow(f,ap)
        (ap,found) = find_path(ag)

def rep(x,i,sigma):
    if x not in sigma:
        sigma[x] = i
    return sigma[x]

def main():
    """
    rep et sigma permettent de traiter les trous dans la numérotation des noeuds et l'utilisation de s
    simplifie la vie.
    """

    g = graph(N)
    sigma = {}
    for i in range(N):
        x,y,w = DATA[i]
        rx = rep(x,i,sigma)
        ry = rep(y,i,sigma)
        g.add_edge(rx,ry,w)
        g.add_edge(ry,rx,w)
    p = widest_path(g,'s',1000)
    print(p)
    
main()

