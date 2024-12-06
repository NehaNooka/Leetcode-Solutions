class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned=set(banned)
        total_sum=ans=0
        for i in range(1,n+1):
            if i not in banned:
                total_sum=total_sum+i
                if total_sum>maxSum:
                    break
                ans+=1
        return ans
        