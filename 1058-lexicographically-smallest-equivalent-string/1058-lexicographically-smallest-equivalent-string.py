class Solution:
    def __init__(self):
        self.parent=[]
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.parent=[i for i in range(26)]

        #union
        for a,b in zip(s1,s2):
            pa=self.find(ord(a)-ord('a'))
            pb=self.find(ord(b)-ord('a'))

            if pa<pb:
                self.parent[pb]=pa
            else:
                self.parent[pa]=pb

        result=[]
        for ch in baseStr:
            mapped=chr(self.find(ord(ch)-ord('a')) + ord('a'))
            result.append(mapped)

        return ''.join(result)

        