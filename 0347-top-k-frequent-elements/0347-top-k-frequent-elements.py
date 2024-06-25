class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        ans=[]
        sorted_counter = sorted(c.most_common(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            ans.append(sorted_counter[i][0])
        return ans