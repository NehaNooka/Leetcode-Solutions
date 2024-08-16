class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res=0
        small,large=arrays[0][0],arrays[0][-1]
        for i in range(1,len(arrays)):
            res=max(large-arrays[i][0],arrays[i][-1]-small,res)
            small=min(small,arrays[i][0])
            large=max(large,arrays[i][-1])
        return res
