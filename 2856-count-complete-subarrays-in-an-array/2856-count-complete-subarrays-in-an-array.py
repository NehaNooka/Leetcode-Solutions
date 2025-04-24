class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count=len(set(nums))
        l,res=0,0
        freq=defaultdict(int)
        for r in range(len(nums)):
            freq[nums[r]]+=1
            while len(freq)==count:
                res+=len(nums)-r
                freq[nums[l]]-=1
                if freq[nums[l]]==0:
                    del(freq[nums[l]])
                l+=1
        return res
        