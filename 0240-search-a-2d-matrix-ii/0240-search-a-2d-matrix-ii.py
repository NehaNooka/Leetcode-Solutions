class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])
        x,y=0,COLS-1
        while x<ROWS and y>=0:
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]>target:
                y-=1
            else:
                x+=1
        return False
        