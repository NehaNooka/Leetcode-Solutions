class Solution:
    def countPrimes(self, n: int) -> int:  
        if n<=2: return 0
        res=[True]* n
        i=2
        while (i*i)<n:
            if res[i]:
                for j in range(i*i, n,i):
                    res[j]=False
            i+=1
        return res.count(True)-2
        