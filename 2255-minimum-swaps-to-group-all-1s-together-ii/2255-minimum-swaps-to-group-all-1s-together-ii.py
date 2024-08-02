class Solution:
    def minSwaps(self, nums: List[int]) -> int:        
        one_count=sum(n for n in nums)
        N=len(nums)
        window_ones= max_window_ones=0
        l=0
        for r in range(2*N):
            if nums[r % N]:
                window_ones+=1
            if r-l+1 > one_count:
                window_ones-=nums[l % N]
                l+=1
            max_window_ones=max(max_window_ones,window_ones)

        return one_count-max_window_ones

        