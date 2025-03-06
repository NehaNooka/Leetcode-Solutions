class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        sq=(n*n)+1
        nums=set([i for i in range(1,sq)])
        res=[]
        for i in range(n):
            for j in range(len(grid[0])):
                if grid[i][j] in nums:
                    nums.remove(grid[i][j])
                else:
                    res.append(grid[i][j])
        return res+list(nums)
