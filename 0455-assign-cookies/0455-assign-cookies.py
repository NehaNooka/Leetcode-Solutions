class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=0
        for cSize in s:
            if cSize >= g[i]:
                i+=1
                if i==len(g): break
        return i
        