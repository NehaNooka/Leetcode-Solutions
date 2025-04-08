class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res=0
        for i in range(0,len(nums),3):
            if len(nums[i:])==len(set(nums[i:])):
                return res
            res+=1
        return res
        