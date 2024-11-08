class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c=len(matrix),len(matrix[0])

        rows,cols=[False]*r,[False]*c

        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rows[i]=True
                    cols[j]=True
        
        for i in range(r):
            for j in range(c):
                if rows[i] or cols[j]:
                    matrix[i][j]=0