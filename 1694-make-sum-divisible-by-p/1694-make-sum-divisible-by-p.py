class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total=sum(nums)
        rem=total%p

        if rem==0: return 0

        cur_sum=0
        remain_to_idx={0:-1}
        res=len(nums)
        for i,n in enumerate(nums):
            cur_sum =(cur_sum+n)%p
            prefix=(cur_sum-rem+p)%p
            if prefix in remain_to_idx:
                length=i-remain_to_idx[prefix]
                res=min(res,length)
            remain_to_idx[cur_sum]=i
        
        return -1 if res==len(nums) else res

        

             

        