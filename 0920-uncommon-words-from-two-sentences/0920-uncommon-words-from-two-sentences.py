class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1= Counter(s1.split(" "))
        s2 = Counter(s2.split(" "))
        res=[]
        for k in s1:
            if s1[k]==1 and k not in s2:
                res.append(k)
        for k in s2:
            if s2[k]==1 and k not in s1:
                res.append(k)
        return res

        