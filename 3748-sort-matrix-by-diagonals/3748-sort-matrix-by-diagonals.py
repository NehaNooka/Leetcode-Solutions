class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        diag=defaultdict(list)
        n=len(grid)

        for r in range(n):
            for c in range(n):
                diag[r-c].append(grid[r][c])
        
        for i in diag:
            diag[i].sort(reverse=(i>=0))
        
        for r in range(n):
            for c in range(n):
                grid[r][c]=diag[r-c].pop(0)
        return grid

        