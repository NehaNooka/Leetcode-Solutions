class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res=0
        count=defaultdict(list)
        for i,v in enumerate(nums):
            if v in count:
                for val in count[v]:
                    if (i*val)%k==0:
                        res+=1
            count[v].append(i)
        return res
        