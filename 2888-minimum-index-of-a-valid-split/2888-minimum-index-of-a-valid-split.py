class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count=Counter(nums)
        maxK,maxV=-1,-1
        for k,v in count.items():
            if v>maxV:
                maxK,maxV=k,v
        countK=0
        n=len(nums)
        for i in range(n-1):
            if nums[i]==maxK:
                countK+=1
            if  countK >(i+1)//2 and (maxV-countK) >(n-(i+1))//2:
                return i

        return -1

