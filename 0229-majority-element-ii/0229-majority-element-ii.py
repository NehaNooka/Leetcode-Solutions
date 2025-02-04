class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N=len(nums)//3
        res=set()
        count=defaultdict(int)
        for num in nums:
            count[num]+=1
            if count[num]>N: res.add(num)
        return list(res)
        