class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visit=[0]*(len(nums)+1)
        visit[0]=1

        for num in nums:
            if 0<num<len(visit):
                visit[num]=1
        
        for i in range(len(visit)):
            if visit[i]==0: return i
        
        return len(nums)+1
            

        