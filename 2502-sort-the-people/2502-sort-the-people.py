class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for name,height in zip(names,heights):
            d[height]=name
        
        heights.sort(reverse=True)
        res=[]
        for h in heights:
            res.append(d[h])
        
        return res
        