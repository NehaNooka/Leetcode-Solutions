class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        full_rounds=time// (n-1)

        extra_rem=time % (n-1)

        if full_rounds%2==0:
            return extra_rem+1
        else:
            return n-extra_rem




        