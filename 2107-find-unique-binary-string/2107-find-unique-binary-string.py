class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])
        nums=set(nums)
        def backtrack(i,ans):
            if i==n:
                if ans not in nums:
                    return ans
                else: return None

            result=backtrack(i+1,ans+'0')
            if result: return result

            result=backtrack(i+1,ans+'1')
            if result: return result

            return None
        return backtrack(0,'')
        