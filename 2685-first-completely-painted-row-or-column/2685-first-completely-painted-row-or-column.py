class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        R,C=len(mat),len(mat[0])
        indexes={}
        for i in range(R):
            for j in range(C):
                indexes[mat[i][j]]=(i,j)
        rows=[0]*R
        cols=[0]*C
        for i,v in enumerate(arr):
            r,c=indexes[v]
            rows[r]+=1
            cols[c]+=1
            if rows[r]==C or cols[c]==R:
                return i
            
        