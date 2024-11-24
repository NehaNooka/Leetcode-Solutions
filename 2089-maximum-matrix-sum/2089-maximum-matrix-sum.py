class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res=0
        neg_cnt=0
        min_val=float('inf')
        for r in matrix:
            for c in r:
                res+=abs(c)
                min_val=min(min_val,abs(c))
                if c<0:
                    neg_cnt+=1
        
        if neg_cnt%2:
            res-=(2*min_val)
        return res

        