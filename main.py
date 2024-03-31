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

def dijkstra (g,x):
    bag = heap()
    bag.push(0,x)