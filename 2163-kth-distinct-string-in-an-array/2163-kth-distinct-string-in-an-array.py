class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res=[]
        counter= Counter(arr)
        for c in arr:
            if counter[c]==1:
                res.append(c)
        return res[k-1] if len(res) >= k else ""
        
