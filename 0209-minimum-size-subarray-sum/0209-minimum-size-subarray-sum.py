class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target: return 0
        res=len(nums)
        l=total=0
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                res=min(res,r-l+1)
                total-=nums[l]
                l+=1
        return res

        