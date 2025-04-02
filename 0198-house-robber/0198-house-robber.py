class Solution:
    def rob(self, nums: List[int]) -> int:
        res=[-1]*len(nums)
        def dfs(i):
            if i>= len(nums): return 0
            if res[i]!=-1: return res[i]
            res[i]=max(dfs(i+1) ,nums[i]+dfs(i+2))
            return res[i]
        return dfs(0)
