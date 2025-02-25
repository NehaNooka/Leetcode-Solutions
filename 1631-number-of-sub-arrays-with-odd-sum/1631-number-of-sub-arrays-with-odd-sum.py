class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum, odd_cnt, even_cnt, res=0,0,0,0
        MOD=10**9+7

        for n in arr:
            cur_sum+=n

            if cur_sum%2: #odd
                res=(res+1+even_cnt) %MOD
                odd_cnt+=1
            else: #even
                res=(res+odd_cnt)% MOD
                even_cnt+=1
        return res


        