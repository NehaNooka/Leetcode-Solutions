class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapping=defaultdict(int)
        for i,c in enumerate(s):
            mapping[c]=i
        res=[]
        size,end=0,0
        for i,c in enumerate(s):
            size+=1
            end=max(end,mapping[c])

            if i==end:
                res.append(size)
                size=0
        return res


        