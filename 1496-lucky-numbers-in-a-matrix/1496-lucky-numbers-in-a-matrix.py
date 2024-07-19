class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        sm_row=[]
        for ma in matrix:
            sm_row.append(min(ma))
        
        ans=[]
        for i in range(len(matrix[0])):
            col=0
            for j in range(len(matrix)):
                temp= matrix[j][i]
                col = max(col,temp)
            if col in sm_row:
                ans.append(col)
                return ans
        
