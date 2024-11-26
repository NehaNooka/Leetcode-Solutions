class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graphSet=set()
        for u,v in edges:
            graphSet.add(v)

        nodes=set([n for n in range(n)])
        if len(nodes)-len(graphSet) >1: return -1

        return sum(nodes)-sum(graphSet)
        