class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        res= float('inf')
        for val in range(1,7):
            topSwap,botSwap=0,0
            valid=True
            for t,b in zip(tops,bottoms):
                if t!=val and b!=val: 
                    valid=False
                    break
                if t!=val:  topSwap+=1
                if b!=val:  botSwap+=1
            
            if valid==True:
                res=min(res, topSwap,botSwap)
        return -1 if res==float('inf') else res