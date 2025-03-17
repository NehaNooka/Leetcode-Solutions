class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c=Counter(nums)
        n=len(nums)//2
        for k,v in c.items():
            if  v%2: return False
        return True

        