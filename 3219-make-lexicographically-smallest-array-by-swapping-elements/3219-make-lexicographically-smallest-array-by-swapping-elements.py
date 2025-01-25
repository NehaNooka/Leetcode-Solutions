class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups=[]
        group_num={}

        for num in sorted(nums):
            if not groups or abs(num-groups[-1][-1])>limit:
                groups.append(deque())
            groups[-1].append(num)
            group_num[num]=len(groups)-1
        
        res=[]
        for n in nums:
            j=group_num[n]
            res.append(groups[j].popleft())
        return res
        