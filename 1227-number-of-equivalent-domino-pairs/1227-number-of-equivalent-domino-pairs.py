class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count,res={},0
        for a,b in dominoes:
            if a>b: a,b=b,a
            if (a,b) in count:
                res+= count[(a,b)]
                count[(a,b)]+=1
            else:
                count[(a,b)]=1
        return res
        