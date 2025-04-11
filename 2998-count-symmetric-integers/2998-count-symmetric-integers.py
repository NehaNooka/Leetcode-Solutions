class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res=0
        def count_all(s):
            return sum(int(c) for c in s)
        for i in range(low,high+1):
            num=str(i)
            if len(num)%2: continue
            if count_all(num[:len(num)//2]) == count_all(num[len(num)//2:]): res+=1
        return res
        