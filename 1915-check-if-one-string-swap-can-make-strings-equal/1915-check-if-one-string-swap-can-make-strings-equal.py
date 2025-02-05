class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1)!=Counter(s2): return False
        if s1==s2: return True
        idx=-1
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if idx==-1:
                    idx=i
                else:
                    if not(s1[idx]==s2[i] and s1[i]==s2[idx]): return False        
        return True