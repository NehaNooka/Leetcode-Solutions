class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead
        1  2  3             
        4  5  6
        7  8  9 

        After transpose, it will be swap(matrix[i][j], matrix[j][i])
        1  4  7
        2  5  8
        3  6  9

        Then flip the matrix horizontally. (swap(matrix[i][j], matrix[i][matrix.length-1-j])
        7  4  1
        8  5  2
        9  6  3       
        """
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i, len(matrix[0])):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reverse_rows(matrix):
            for r in range(len(matrix)):
                left, right = 0, len(matrix) - 1
                while left < right:
                    matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                    left += 1
                    right -= 1

        transpose(matrix)
        reverse_rows(matrix)