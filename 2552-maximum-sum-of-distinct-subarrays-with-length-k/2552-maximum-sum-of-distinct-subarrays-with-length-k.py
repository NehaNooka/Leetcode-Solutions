class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums)<k:
            return 0
        max_sum,cur_sum=0,0
        distinct_ele=set()
        l=0
        for r in range(len(nums)):
            while nums[r] in distinct_ele or len(distinct_ele)>=k:
                distinct_ele.remove(nums[l])
                cur_sum-=nums[l]
                l+=1

            distinct_ele.add(nums[r])
            cur_sum+=nums[r]

            if r-l+1==k:
                max_sum=max(max_sum,cur_sum)
            
        return max_sum




        