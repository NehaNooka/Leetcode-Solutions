class UnionFind:
    def __init__(self,n):
        self.par=list(range(n))
        self.size=[1]*n
    
    def find(self,x):
        if x!=self.par[x]:
            self.par[x]=self.find(self.par[x])
        return self.par[x]
    
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)

        if x!=y:
            if self.size[x]<self.size[y]:
                self.par[x]=y
                self.size[y]+=self.size[x]
            else:
                self.par[y]=x
                self.size[x]+=self.size[y]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        #1. Build Components
        uf=UnionFind(n)
        for u,v,w in edges:
            uf.union(u,v)
        
        #2. Get cost of each component
        comp_cost={}
        for u,v,w in edges:
            root=uf.find(u)
            if root not in comp_cost:
                comp_cost[root]=w
            else:
                comp_cost[root]&=w

        # 3. Queries
        res=[]
        for src,dst in query:
            r1,r2=uf.find(src),uf.find(dst)
            if r1!=r2:
                res.append(-1)
            else:
                res.append(comp_cost[r1])
        return res





        