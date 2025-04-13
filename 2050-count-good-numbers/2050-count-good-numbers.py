class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD= 10**9+7
        def power(base,exp):
            res=1
            bas=MOD
            while exp>0:
                if exp%2==1:
                    res=(res*base)% MOD
                base=(base*base)%MOD
                exp//=2
            return res

        even=(n+1)//2
        odd=n//2
        ans= (power(5,even)*power(4,odd))% MOD
        return ans        