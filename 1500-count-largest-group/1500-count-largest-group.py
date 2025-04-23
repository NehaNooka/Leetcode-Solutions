class Solution:
    def countLargestGroup(self, n: int) -> int:
        count=defaultdict(int)
        maxL,res=0,0
        for i in range(1,n+1):
            sum_i = sum(int(c) for c in str(i))
            count[sum_i] +=1
            maxL= max(maxL,count[sum_i])
        
        for k,v in count.items():
            if v==maxL: res+=1

        return res
