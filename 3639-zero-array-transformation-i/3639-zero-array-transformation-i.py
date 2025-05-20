class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n=len(nums)
        diff=[0]*(n+1)
        for l,r in queries:
            diff[l]-=1
            if (r+1)<n: diff[r+1]+=1
        sum_val=0
        for i in range(n):
            sum_val+=diff[i]
            if nums[i]> -sum_val: return False
        return True
        