class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n=len(nums)
        prefix_sum=[0]*n
        prefix_sum[0]=1

        for i in range(1,n):
            if (nums[i]&1)==(nums[i-1]&1):
                prefix_sum[i]=1
            else:
                prefix_sum[i]=prefix_sum[i-1]+1
        

        ans=[]
        for start,end in queries:
            size=end-start+1

            if prefix_sum[end]>=size:
                ans.append(True)
            else:
                ans.append(False)
        return ans

        