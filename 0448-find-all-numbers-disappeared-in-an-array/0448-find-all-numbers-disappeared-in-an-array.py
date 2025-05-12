class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        lookup=set(nums)
        for n in range(1,len(nums)+1):
            if n not in lookup:
                res.append(n)
        return res

        