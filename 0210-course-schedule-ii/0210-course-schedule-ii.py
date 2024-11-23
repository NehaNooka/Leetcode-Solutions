class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq={i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            prereq[crs].append(pre)
        
        visit,cycle=set(),set() # total ele visited, current cycle ele
        res=[]
        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True
            
            cycle.add(i)
            for pre in prereq[i]:
                if not dfs(pre):
                    return False
            cycle.remove(i)
            visit.add(i)
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i): return []
        return res
        



