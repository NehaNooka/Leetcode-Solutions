class Solution:
    def sumZero(self, n: int) -> List[int]:
        res=[]
        for i in range(1,n):
            res.append(i)
        last=(n*(n-1))//2
        res.append(-last)
        return res

        