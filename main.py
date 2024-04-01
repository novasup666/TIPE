class heap:

    def __init__(self) -> None:
        self.data = []
        self.size = 0

    def is_empty(self):
        return (self.size == 0)

    def switch(self,i1,i2):
        assert(0 <= i1 < self.size)
        assert(0 <= i2 < self.size)
        tmp = self.data[i1]
        self.data[i1] = self.data[i2]
        self.data[i2] = tmp


    def sift_up (self,index):
        p = self.data[index][0]
        while self.data[int((index-1)/2)][0] > p:
            self.switch(index,int((index-1)/2))

    def sift_down(self,index):
        k = index
        k_prime = k
        if 2*k+1 < self.size and self.data[2*k+1][0] < self.data[k_prime][0]:
            k_prime = 2*k+1 
        if 2*k+2 < self.size and self.data[2*k+2][0] < self.data[k_prime][0]:
            k_prime = 2*k+2
        while k!=k_prime:
            self.switch(k,k_prime)
            k = k_prime
            if 2*k+1 < self.size and self.data[2*k+1][0] < self.data[k_prime][0]:
                k_prime = 2*k+1 
            if 2*k+2 < self.size and self.data[2*k+2][0] < self.data[k_prime][0]:
                k_prime = 2*k+2


    def push(self, p,v):
        self.data.append((p,v))
        self.size += 1
        self.sift_up(self.size-1)
    
    def pop (self):        
        self.switch(0, self.size-1)
        res = self.data.pop()
        self.size-=1
        self.sift_down(0)
        return res

class graph:
    def __init__(self,n) -> None:
        self.size = n
        self.graph = {}
    
    def add_edge(self,x,y,w):
        self.graph[x].append((y,w))

DATA = [('s',2,4),('s',2,3),('s',3,4),('s',4,4),('s',5,3),('s',6,3),('s',7,7),('s',8,3),('s',9,2),('s',10,2),(0,1000,3),(1,11,5),(1,45,5),(2,45,5),(45,44,5),(44,43,5),(43,41,5),(2,3,4),(3,4,4),(4,5,4),(5,42,4),(41,42,4),(42,6,4),(41,40,5),(40,46,2),(46,38,6),(38,37,6),(6,37, 5),(6,36,5),(37,36,5),(7,36,7),(36,39,12),(38,39,3),(39,1001,12),(39,20,4),(36,35,3),(35,34,3),(19,34,3),(8,19,6),(19,23,1),(24,23,4),(18,24,3),(23,25,3),(23,27,4),(27,29,4),(29,21,4),(20,21,11),(21,54,3),(54,55,3),(25,31,4),(31,32,4),(25,26,5),(26,28,5),(29,28,4),(28,30,4),(30,33,3),(28,22,4),(21,22,7),(22,33,7),(33,1002,8),(51,33,7),(53,51,2),(52,53,2),(52,49,5),(55,52,2),(54,49,3),(49,51,3),(22,49,5),(10,12,5),(10,9,5),(9,16,4),(12,15,4),(12,11,5),(15,17,3), (16,17,5),(16,18,3),(17,18,4) ]

"""
Ici on écrira dijkstra
def dijkstra (g,x):
    bag = heap()
    bag.push(0,x)
    
"""

def main():
    g = graph
    for i in range(len(DATA)):
        x,y,w = DATA[i]
        g.add_edge(x,y,w)
        g.add_edge(y,x,w)
    