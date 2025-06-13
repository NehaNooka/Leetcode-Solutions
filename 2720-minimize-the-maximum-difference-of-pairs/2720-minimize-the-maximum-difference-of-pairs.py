class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n=len(nums)
        l,r=0,nums[n-1]-nums[0]


        def countValidPairs(nums,diff):
            i,count=0,0
            while i<n-1:
                if nums[i+1]-nums[i]<=diff:
                    count+=1
                    i+=1
                i+=1
            return count

        while l<r:
            mid=(l+r)//2

            if countValidPairs(nums,mid)>=p:
                r=mid
            else:
                l=mid+1
        return l
        