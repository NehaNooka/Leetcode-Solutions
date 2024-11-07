class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for num in range(n+1):
            one_count=0
            while num:
                one_count+=1 if num &1 else 0
                num=num>>1
            res.append(one_count)
        return res