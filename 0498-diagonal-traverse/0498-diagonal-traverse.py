class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res=[]
        ROWS,COLS=len(mat),len(mat[0])
        r,c=0,0
        going_up=True
        while len(res)<ROWS*COLS:
            if going_up:
                while r>=0 and c<COLS:
                    res.append(mat[r][c])
                    r-=1
                    c+=1
                if c==COLS:
                    c-=1
                    r+=2
                else:
                    r+=1
                going_up=False
            else:
                while r<ROWS and c>=0:
                    res.append(mat[r][c])
                    r+=1
                    c-=1
                if r==ROWS:
                    c+=2
                    r-=1
                else:
                    c+=1
                going_up=True
        return res          



