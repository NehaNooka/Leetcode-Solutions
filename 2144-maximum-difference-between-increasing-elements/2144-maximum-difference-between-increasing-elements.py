class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        small=nums[0]
        res=-1
        for ele in nums:
            if ele<small:
                small=ele
            elif ele>small:
                res=max(res, ele-small)
        return res

        