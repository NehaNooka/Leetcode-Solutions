class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(list)
        for a,b in prerequisites:
            adj[b].append(a)

        preReqMap={}

        def dfs(crs):
            if crs not in preReqMap:
                preReqMap[crs]=set()
                for prereq in adj[crs]:
                    preReqMap[crs]|= dfs(prereq)
                preReqMap[crs].add(crs)
            return preReqMap[crs]

        for crs in range(numCourses):
            dfs(crs)
        
        res=[]
        for u,v in queries:
            if u in preReqMap[v]:
                res.append(True)
            else: res.append(False)
        return res


