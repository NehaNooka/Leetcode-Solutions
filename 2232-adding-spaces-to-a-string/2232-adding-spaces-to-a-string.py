class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        afterS=[]
        i=0
        for j in spaces:
            afterS.append(s[i:j])
            i=j
        afterS.append(s[j:])
        return ' '.join(afterS)
        