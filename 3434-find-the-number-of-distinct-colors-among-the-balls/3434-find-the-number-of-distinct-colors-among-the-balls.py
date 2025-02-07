class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorMap=defaultdict(int)
        numMap=defaultdict(int)
        res=[]
        for node,color in queries:
            if node in numMap:
                prevColor=numMap[node]
                colorMap[prevColor]-=1
                if not colorMap[prevColor]:
                    del(colorMap[prevColor])
            colorMap[color]+=1
            numMap[node]=color
            res.append(len(colorMap))
        return res
        