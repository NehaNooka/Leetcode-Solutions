class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        safe={}
        res=[]

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i]=False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safe[i]=True
            return safe[i]

        for i in range(n):
            if dfs(i):
                res.append(i)
        return res


        