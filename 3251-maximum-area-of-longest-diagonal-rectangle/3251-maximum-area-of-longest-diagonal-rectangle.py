class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiag,res=0,0

        for l,w in dimensions:
            currDiag=l*l + w*w
            if currDiag>maxDiag or (currDiag==maxDiag and l*w>res):
                maxDiag=currDiag
                res=l*w
        return res
        