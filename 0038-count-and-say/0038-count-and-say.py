class Solution:
    def countAndSay(self, n: int) -> str:
        prev='1'
        if n==1: return prev
        def getRLE(n):
            curr,count=n[0],1
            res=""
            for i in range(1,len(n)):
                if  n[i-1]==n[i]:
                    count+=1
                else:
                    res+=  str(count)+ curr
                    curr=n[i]
                    count=1
            res+=  str(count) + curr
            return res

        for i in range(2,n+1):
            prev=getRLE(prev) 
        return prev

        